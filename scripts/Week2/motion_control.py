#!/usr/bin/python
import rospy
from ackermann_msgs.msg import *
from sensor_msgs.msg import *
from nav_msgs.msg import *
import sys, math
from student.msg import blob_detect
from std_msgs.msg import Float32MultiArray
from cv_bridge import CvBridge, CvBridgeError
import time


class ObjectDetectorNode:

    def __init__(self):
	
	self.bridge = CvBridge()
        self.refresh_count = 0
        self.refresh_count = rospy.get_param('refresh_count', default=self.refresh_count)
        self.desired_distance = 0.45
        self.desired_distance = rospy.get_param('desired_distance', default=self.desired_distance)
        self.threshold = 0.07
        self.rolling_sum = 0
	self.turnStart = 0.0

        self.before_e = 0
        self.is_running = True #always
        self.is_right = True
        self.stopped = False
        self.blob_found = False
        self.blob_points = None
        self.color = None

        self.color_error = 0
        self.ddes = 0
        self.dhat = 0
        self.blob_height = 0
        self.ready_to_wall_detect = False #temp

        self.img_width = 0
        self.img_height = 0

        self.drive_pub = rospy.Publisher("/vesc/ackermann_cmd_mux/input/navigation", AckermannDriveStamped,queue_size=10)

        self.vision = rospy.Subscriber("/scan", LaserScan, self.drive_control)
        self.joystick = rospy.Subscriber("/vesc/joy", Joy, self.handle_buttons)
        self.blob_detect_sub = rospy.Subscriber("/blob_info", blob_detect, self.blob_callback)
        self.zed_camera = rospy.Subscriber("/camera/rgb/image_rect_color", Image, self.zed_cam_callback) 	

        self.header = std_msgs.msg.Header()
        self.header.stamp = rospy.Time.now()
        self.STOP = AckermannDriveStamped(self.header, AckermannDrive(steering_angle=0.0, speed=0.0))
        rospy.loginfo("Moving forward...")

    def handle_buttons(self, msg):
        a_pressed = msg.buttons[0]
        b_pressed = msg.buttons[1]
        third_but_pressed = msg.buttons[3]
        if a_pressed == 1:
            self.is_right = not self.is_right
            rospy.sleep(float(sys.argv[4]))
        if b_pressed == 1:
            self.stopped = True
        if third_but_pressed == 1:
	    self.is_running = True	

    def drive_control(self, msg):
        if self.is_running:
            if self.stopped:
                self.drive_pub.publish(self.STOP)
	        rospy.loginfo("Car Stopped")
            else:
		#img height
		img_height = self.img_height
		#self.blob_height
		print "blob height;",str(self.blob_height)
		print "img height:", str(img_height)
		height_ratio = float(self.blob_height) / float(img_height)
		print "height ratio:", str(height_ratio)
		print "COlor:", self.color
		threshold = .1
		if height_ratio < threshold and not self.ready_to_wall_detect:

			#COLOR DRIVING		
			print ("Color Driving")
			col_error = self.ddes - self.dhat
			print "Color Error:",col_error
			color_steering_angle = self.pid_color_control(col_error)
		  	drive_command_color = AckermannDriveStamped(self.header, AckermannDrive(steering_angle=color_steering_angle, speed=2.0))
		    	self.drive_pub.publish(drive_command_color)
		    	#COLOR DRIVING END
		elif height_ratio >= threshold or self.turnStart:
			print "Wall Following"
			#rospy.sleep(1)
			#WALL DETECTION START
			if self.color == "red" and self.ready_to_wall_detect:
		            rospy.loginfo("Tracking left wall")
		            self.is_right = True
		            #self.ready_to_wall_detect = True
			    turn_abr_cmd = AckermannDriveStamped(self.header, AckermannDrive(steering_angle=1.0, speed=2.0))
			    self.drive_pub.publish(turn_abr_cmd)
			elif self.color == "green" and self.ready_to_wall_detect:
		            rospy.loginfo("Tracking right wall")
		            self.is_right = False
		            #self.ready_to_wall_detect = True
			    turn_abr_cmd = AckermannDriveStamped(self.header, AckermannDrive(steering_angle=-1.0, speed=2.0))			    
			    self.drive_pub.publish(turn_abr_cmd)
			else:
	    		    print "Not Detecting Color"

			if not self.turnStart:
			    self.turnStart = time.time()

			if time.time() - self.turnStart > .75:
			    self.ready_to_wall_detect = True
		
		        if self.ready_to_wall_detect:
		 	    self.refresh_count += 1

		        if self.is_right:
		            pts = msg.ranges[200:540] # [170:200]
		            pt_one = msg.ranges[180] 
		            pt_two = msg.ranges[300]
		        else:
		            pts = msg.ranges[540:900] # [880:910]
		            pt_one = msg.ranges[900]
		            pt_two = msg.ranges[780]
		    	
		        error = self.desired_distance - min(pts)
		        d_hat = ((pt_one*pt_two)/(2*math.sqrt((math.pow(pt_one, 2) + math.pow(pt_two, 2) - math.sqrt(3)*pt_one*pt_two))))
		        error_two = self.desired_distance - d_hat
		        error_new = (error + error_two)/2
			error_new = error
		        if self.refresh_count == 1:
		            self.before_e = error

		        # new_steering_angle = self.bang_bang_controller(error)
		        # new_steering_angle = self.bang_bang_with_threshold(error)
		        new_steering_angle = self.pid_controller(error_new)
		        drive_command = AckermannDriveStamped(self.header, AckermannDrive(steering_angle=new_steering_angle, speed=2.0))
		        self.drive_pub.publish(drive_command)
		        #WALL DETECTION END

    def zed_cam_callback(self, img):
        img_data = self.bridge.imgmsg_to_cv2(img)
        self.img_width, self.img_height, channels = img_data.shape
	
    def blob_callback(self, data):
	
        self.blob_height = float(data.height.data)
        first_pts = data.location
        blob_x = self.img_width * first_pts.x
        blob_y = self.img_height * first_pts.y

        curr_x = self.img_width / 2
        curr_y = self.img_height / 2


        self.color = data.color.data
	
        self.ddes = curr_x
        self.dhat = blob_x

    def pid_color_control(self, error):
	return float(sys.argv[5]) * error

    def pid_controller(self, error):
        rospy.loginfo(error)
        return self.proportion(error, self.is_right) + self.differential(error, 40.0, self.is_right) + self.integral(error, self.is_right)

    def proportion(self, error, is_right):
        if is_right:
            return float(sys.argv[1]) * float(error)
        else:
            return -1 * float(sys.argv[1]) * float(error)

    def differential(self, error, hz, is_right):
        delta_time = 1 / hz
        edot = float(error - self.before_e) / float(delta_time)
        kd = float(sys.argv[3])
        self.before_e = error
	if is_right:
            return kd * edot
        else:
            return -kd * edot

    def integral(self, error, is_right):
        self.rolling_sum += error
        ki = float(sys.argv[2])
        if is_right:
            return ki * self.rolling_sum
        else:
            return -1 * ki * self.rolling_sum

if __name__ == "__main__":
	rospy.init_node("object_detector_node")
   	node = ObjectDetectorNode()
    	rospy.spin()
