#!/usr/bin/env python

#general imports
import rospy as rsp
import numpy as np

#node-specific imports
from sensor_msgs.msg import Image
from std_msgs.msg import *
from student.msg import blob_detect
from geometry_msgs.msg import Point
from cv_bridge import CvBridge, CvBridgeError
import cv2


class BlobPublisher:

	def __init__(self):

		self.bridge = CvBridge() #allows us to convert to/from cv2
		
		#publishers
		self.blob_pub = rsp.Publisher("image_echo", Image, queue_size=10) #publishing altered camera image 
		self.loc_size_pub = rsp.Publisher("blob_info", blob_detect, queue_size=10) #publishing custom message type (blob_detect)
		
		#subscriber
		self.blob_img = rsp.Subscriber("/camera/rgb/image_rect_color", Image, self.detect_img) #subscribing to camera image
		
		self.header = std_msgs.msg.Header()

		
	def detect_img(self, img):
		img_data = self.bridge.imgmsg_to_cv2(img) #converts image to cv2 so it can be processed/altered

		processed_img_cv2 = self.process_img(img_data)
		processed_img = self.bridge.cv2_to_imgmsg(processed_img_cv2, "bgr8") #converting image back to original format

		self.blob_pub.publish(processed_img) #publishing image to image_echo topic so it can be viewed in rqt_image_graph

	def process_img(self, img):
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #converts colors to hsv values 
		
		# GETTING GREEN CONTOURS
		
		# setting up hsv ranges
		hue_green_min = 100
		hue_green_max = 154
		sat_green_min = .4
		sat_green_max = 1
		val_green_min = .15
		val_green_max = 1
    
    #creating mask and contours and drawing the contours on the image
		maskGreen = cv2.inRange(hsv, np.array([hue_green_min / 2, int(sat_green_min * 255),int(val_green_min * 255)]), np.array([hue_green_max / 2, int(sat_green_max * 255), int(val_green_max * 255)]))
		contours_green, hierarchy_green = cv2.findContours(maskGreen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img, contours_green, -1, (120, 0, 0), 4)
		
		# GETTING RED CONTOURS
		
		# setting up hsv ranges
		hue_red_min1 = 225
		hue_red_max1 = 250
		sat_red_min1 = .8
		sat_red_max1 = 1
		val_red_min1 = .7
		val_red_max1 = 1
		
	  #creating mask/contours and drawing contours on image
	 	maskRed = cv2.inRange(hsv, np.array([hue_red_min1 / 2, int(sat_red_min1 * 255), int(val_red_min1 * 255)]), np.array([hue_red_max1 / 2, int(sat_red_max1 * 255), int(val_red_max1 * 255)]))
		contours_red, hierarchy_red = cv2.findContours(maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img, contours_red, -1, (120, 0, 0), 4) #draws contours in blue with a thickness of 4 
		
		blob = blob_detect() # creating instance of custom message type 
		
		officCont = contours_green # setting default contour to green
		if(len(contours_green) == 0): #if there are no green contours, assume red
			officCont = contours_red
			blob.color = "red"
		else:
			blob.color = "green"
			
		try:		
			if len(officCont) != 0:
				contour = officCont[0]
				M = cv2.moments(contour)
				if M['m00'] != 0:
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
					centergr = (cx, cy)
					cv2.circle(img, centergr, 5, (60, 0, 0), -1) #draws circle around center
					x, y, w, h = cv2.boundingRect(contour)	
					cv2.rectangle(img, (x,y), (x+w, y+h), (100, 50, 50), 2) #draws rectangle around contour
					
					#size
					blobSize = w*h
					
					#location
					height = np.size(img, 0)
					width = np.size(img, 1)
					location = Point(float(cx)/float(width), float(cy)/float(height), 0) # center of blob as ratio so if image is a different pixel size it will still be correct
					
					blob.header = self.header
					blob.sizes = Float64(float(blobSize))
					blob.location = location	

					self.loc_size_pub.publish(blob)
			
		except Exception, e:
			print str(e)
			
		return img

if __name__ == "__main__":
  rsp.init_node("blob_pub")
	node = BlobPublisher()
	rsp.spin()
