#!/usr/bin/env python

# general imports for all python nodes
import rospy
import math
import numpy

# node-specific imports
from ackermann_msgs.msg import AckermannDriveStamped # steering messages
from sensor_msgs.msg import LaserScan, Joy # joystick and laser scanner msgs

class WallE():

    angle = 0 #ensure variable is created before use 
    
    def __init__(self):
        #setup the node
        rospy.init_node('wall_bang', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        
        #setting up publisher (published motion commands that will move the robot)
        self.drive = rospy.Publisher('/vesc/ackermann_cmd_mux/input/navigation', AckermannDriveStamped, queue_size=5)
        
        #setting up the subscriber(subscribes to the LiDAR laser scan, set of 1081 points)
        rospy.Subscriber('scan', LaserScan, self.callback)
        
        # set control parameters
        speed = 0.5 # constant travel speed in meters/second
        dist_trav = 20.0 # meters to travel in time travel mode (distance to travel before stopping)
        
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
            self.drive.publish(drive_cmd) # post this message
    
    def getSteerAngle(self, goal, L, begin, end, threshold, fullLeft, fullRight): #gets distance between where the car is currently and where it wants to be
        error = goal-(min(L[begin:end]))
        if(abs(error)<threshold): # if the error is very small, do not turn at all
            return 0
        elif error>0: # car is too far from wall, turn left
            return fullLeft
        else: # (error>0), car is too close to wall, turn right
            return fullRight

    #passed to the subscriber
    def callback(self,msg): 
        self.angle=self.getSteerAngle(.4, msg.ranges, 540, 930, .03, -1, 1) #left wall follow (0 = all the way right in LiDAR scan, 540 = middle, 1081 = all the way left)
        
    def shutdown(self): #is called whenever ctrl-c is hit to make sure the robot stops
        rospy.loginfo("Stopping the robot...")
        self.drive.publish(AckermannDriveStamped())
        rospy.sleep(1)
        
if __name__ == '__main__':
  try:
    WallE()
 except:
    pass
    rospy.loginfo("WallE node terminated.")
