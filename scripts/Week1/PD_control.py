#!/usr/bin/env python

# general imports for all python nodes
import rospy
import math
import numpy

# node specific imports
from ackermann_msgs.msg import AckermannDriveStamped # steering messages
from sensor_msgs.msg import LaserScan, Joy # joystick and laser scanner msgs
from numpy.core.defchararray import lower

class WallE():
    
    #making sure variables are initialized before called 
    angle=0
    e1=0
    e2=0
    
    def clip(self,high,low,value): #used to clip steering angle command
        if high<value:
            return high
        elif value<low:
            return low
        else:
            return value
        
    def getSteerCmd(self, goal, L, begin, end, fullLeft, fullRight):
        error = goal-(min(L[begin:end])) #distance between current and desird distance from wall
        Kp = .7
        Kd = .6
        de= ((self.e1-self.e2)+(error-self.e1))/.2 #rate of change of error vals, used to prevent oscillation
        self.e2=self.e1
        self.e1 = error
        u = Kp*error + Kd*de
        return self.clip(fullLeft, fullRight, u)

    #passed to the subscriber
    def callback(self,msg):
        #get the laser information
        self.angle=self.getSteerCmd(.4, msg.ranges, 200, 540, -1, 1)
        
    def shutdown(self): #makes sure robot is stopped when ctrl-c is pressed
        rospy.loginfo("Stopping the robot...")
        self.drive.publish(AckermannDriveStamped())
        rospy.sleep(1)
    
    def __init__(self):
        #setup the node
        rospy.init_node('wall_bang', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        
        # publisher that sends motion commands
        self.drive = rospy.Publisher('/vesc/ackermann_cmd_mux/input/navigation', AckermannDriveStamped, queue_size=5)
        
        #sets the subscriber
        rospy.Subscriber('scan', LaserScan, self.callback)
        
         # set control parameters
        speed = 2.0 # constant travel speed in meters/second
        dist_trav = 20.0 # meters to travel in time travel mode
        
        # fill out fields in ackermann steering message
        drive_cmd = AckermannDriveStamped()
        drive_cmd.drive.speed = speed
        drive_cmd.drive.steering_angle = self.angle 
        
        # output messages/sec (also impacts latency)
        rate = 10 
        r = rospy.Rate(rate)
        
        # main processing loop (runs for pre-determined duration in time travel mode)
        time = dist_trav / speed
        ticks = int(time * rate) # convert drive time to ticks
        for t in range(ticks):
            drive_cmd.drive.steering_angle=self.angle
            self.drive.publish(drive_cmd) # publishing drive command 
        
if __name__ == '__main__':
  try:
    WallE()
  except:
    pass
    rospy.loginfo("WallE node terminated.")
