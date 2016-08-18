#Week Three: Technical Work

##Goals

Week three had a slightly different format than weeks one and two. Unlike in the previous two weeks, most of the lectures were not relevant to the lab work. Because of this, the academic and challenge goals of the week are noticeably disjoint.

The lectures during week three focused on localization and mapping. Students also learned about several path planning algorithms. The goal was to understand common algorithms that are used to let a robot know where it is in its environment and can be used to develop routes to specific goals.

The weekly challenge did not required groups to implement any localization or mapping functionality. The cars had to drive around for two minutes in an enclosed pen, avoid hitting any obstacles, and identify as many different colored blobs as possible.

##Approach

Although students did not implement localization, mapping, or the SLAM algorithm during the program, they were an important part of the student's conceptual learning for the week. Potential fields were implemented by almost all teams and were relevant to the localization and mapping lectures of the week. 

###Localization

Localization is the process of determining the pose of a robot with respect to an environment it is given a representation of (1). The representation is defined with respect to some external reference frame, such as the robot's starting position or nearby walls, corners, or markings. (15)

Dead reckoning localization uses odometry to estimate the robot's pose with respect to the initial coordinate frame. Dead reckoning has multiple error sources, such as wheel slip, gear backlash, noise from encoders, and sensor or processor quantization errors that accumulate over time to  make the pose less than accurate. (15)

![Dead Reckoning Errors](https://cloud.githubusercontent.com/assets/18174572/17782992/fc071c9a-6543-11e6-9f89-d846b68e9272.png)

Figure 1: Accumulated error from dead-reckoning localization (15)

Landmarks with known reference frame pose embedded in the environment can help cut down on these errors. Landmarks can be natural, such as a wall corner, or artificial, like a surveyor's mark. They also vary in which sensor is able to detect it. Triangulation can be used to estimate pose with respect to two landmarks. (15)

###SLAM Algorithm

The Simultaneous Localization and Mapping Algorithm (SLAM) algorithm allows a robot with no external coordinate reference to use a series of proprioceptive and exteroceptive (internal and external) measurements taken as it moves through an unknown environment to create a map of said environment (15). The robot is also able to localize itself with respect to the map it generates.

SLAM is also most effective when landmarks are used. Localization based on environment features minimizes robot pose uncertainty and thus the uncertainty of the map (15). Laser scans or camera data could both be used to create the map.

###Potential Fields

The potential field method is a form of path planning algorithm. The key idea of potential field algorithms is that the robot travels through a space such that it is attracted to a goal region and repelled from any obstacles (16). This can be implemented using localization or as a reactive algorithm. The latter was most relevant to the student's goals for the week. 

Vectors are an excellent way to execute a potential field algorithm. The LiDAR scanner, creates 1081 data points containing the distance between the car and the nearest obstacle in that direction. Each of these points can be interpreted as vectors directed at the car; the shorter the distance between the car and the obstacle, the stronger the force of the vector. This effectively repels the car away from any obstacles. However, in reactive planning, there is no 'goal region' as the robot has no idea of its pose with respect to the environment, so the robot is not being attracted to anything, only repelled. To fix this, a large driving charge can be placed directly behind the robot to move it forward. This method works well when the robot is just trying to explore and avoid obstacles as was the goal in week three's challenge. 

The following formulas can be used to find the repulsive force of a single point: 

                            |Ê| = Alaser / r^2                                              (eq. 1)

Where Alaser is some constant charge and r is the distance of the car to the obstacle for that particular point. By using this equation for every point and summing the results, one can obtain the total repulsive force. 

A major advantage of the potential field algorithm is that when a car gets extremely close to an obstacle, the repelling charge from the obstacle overpowers the driving force which causes the car to back up. This prevents it from getting stuck.

###Challenge Approach

My team decided to use two nodes for the weekly challenge. One would control the cars motion and implement a potential field algorithm. The other would detect and record images of blobs that the car's camera captured. These nodes were completely independent of each other and did not communicate at all. We decided to have two independent nodes because it was not necessary for them to communicate. This week, we focused on perfecting the simplest algorithms that could accomplish our goals. 

We decide to write the motion control first, followed by the vision node. Since we had spent all of last week learning about image processing, we felt more confident in that part of the code and wanted to get the unfamiliar potential field done first. Like the first week, for the most part all members of the group worked through the process together with very little task delegation. Codeshare.io allowed us to all look at the code together without crowding around one computer and was a very useful tool during the week. 

One decision we made before writing the motion node was to add a functionality to help the car get "unstuck" if it ever stopped moving completely. Although rare, sometimes the driving force and the repelling forces equalize, causing the car to stall. To fix this, we chose to add code that told the car to back up if it had not moved for more than two seconds.

We also had to decide how to approach saving images that the vision node captured. The main concern was capturing many images detecting the same blob. The camera publishes multiple images per second, and the same blob would probably be present in several images in a row. It is unnecessary to detect any blob more than one time, so our group had to decide how to prevent repeat recognition from happening. This could be done using odometry or time. We decided to use distance. After the car saved a picture, it would have to travel one meter before capturing another. 


##Process

###Explorer Node

The potential field algorithm was surprisingly simple to implement. The first draft of the code took less than half an hour to write. Other than a few syntax errors, the code was functional right off the bat and just needed tweaking. 

The node subscribed to the 'scan' topic to receive LiDAR data and published steering commands to the 'vesc/ackermann_cmd_mux/input/navigation' topic. For our propelling charge we settled on a value of 4, and the Alaser value was 0.005. These took a lot of testing to figure out. If the propelling charge was not large enough, the car would not move forward, but if it were too large in comparison to the Alaser value, then it would collide with obstacles because their repelling charges would be completely overwhelmed. 

###Blob Search

The blob detection node would look for contours of all four colors and determine the size of the largest of each color. If this size was larger than a predetermined threshold height (100 pixels), then this contour would 'count.' It would be outlined and labeled and a picture of it would be saved. Originally we planned to only detect the largest blob, but by checking blobs of each color against a threshold the car would be able to detect more than one blob at once. 

The node subscribed to the '/camera/rgb/image_rect_color' topic to recieve images and the '/vesc/odom' topic to receive odometry information. It published to the '/image_echo' topic and the '/exploring_challenge' topic, which would publish a string that said what color blobs it detected. Both of thse were used for debugging. 

In order to receive any points in the challenge, the camera image with contours and labels for blobs added had to be saved in the '/home/racecar/challenge_photos' directory. We did this using the OpenCV function cv2.imwrite and naming the image file based on the time at which it was taken.

We had many problems perfecting color bounds for the four different blobs. On the HSV scale, a hue of 0 to 15 is supposed to indicate the color red, but the only way we could get the algorithm to correctly detect red was using a range of 100 to 125. We realized this was inverted (as a hue value around 120 is supposed to be blue, not red), and soon after discovered the problem. The original image was in BGR format, not RGB, so when we used the OpenCV function cv2.cvtColor to switch from RGB to HSV, we were not giving the function the correct starting format. By the time we fixed this however, we had just an hour before the final challenge. Because of this we were very rushed when determining HSV ranges and they were not as accurate as we wanted. 

**Table 1: Color Bounds for Blob Detection**

| Color | Hue Min | Hue Max | Saturation Min | Saturation Max | Value Min | Value Max |
|-------|:-------:|:--------:|:--------------:|:-------------:|:--------:|:----------:|
|Red    |    0     |    15      |     .85           |      1      |      .2      |     .9       |
|Green    |    30     |   75       |      .5          |     1       |     .4       |     1       |
|Yellow   |    0     |    180      |        .3        |     1       |     .745       |    1        |
|Blue    |    100     |   125       |    .4            |      1      |    0        |     .5       |

We tested the vision blob by only running the blob detection node and having it publish to the /image_echo topic and putting different colored blobs in front of the camera to see if it was correctly detecting them.


##Results

In the final challenge, cars were given two minutes to navigate a pen in which red, green, yellow, and blue blobs were randomly dispersed. For each blob the car successfully detected and recorded in an image file, it was awarded ten points. For each collision, two points were deducted. There were also special pink blobs with different images inside of them. If the car was able to successfully identify what the image was, it would be awarded five points.

In the final challenge, car 7, my group's car, detected six blobs (no special blobs) and had just one collision, which ended us with a total score of 58 points. My team received second place overall for this performance. 

The lack of time put into perfecting color ranges was apparent in the images that the vision node produced. Though it correctly identified six blobs, it also detected many things that were not blobs to be blobs and occasionally misidentified a blob as a different color than it actually was.

![sucess](https://cloud.githubusercontent.com/assets/18174572/17710382/00521852-63bb-11e6-83a6-6a10a6911656.png)

Figure 2: Successful detection of blob (10 pts), original image

![Failure](https://cloud.githubusercontent.com/assets/18174572/17710383/00560a02-63bb-11e6-9a59-b3463de206e9.png)

Figure 3: Detection of background as a blob, original image

![Different Failure](https://cloud.githubusercontent.com/assets/18174572/17710379/00388d74-63bb-11e6-8739-9a6b26836600.png)

Figure BLANK 4: Correct detection of green blob and incorrect detection of red blob, original image

From the pictures it was clear that our car could have been more successful at blob detection if we had set the speed to be slightly lower. The images were blurred, which most likely did nothing to help the image processing. The car definitely went faster than necessary as it made at least five full loops around the course in the allotted two minutes. Clearer images could have led to more accurately identified blobs.
