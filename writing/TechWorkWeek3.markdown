#Week Three: Technical Work

##Goals

Week three had a slightly different format than weeks one and two. Unlike in the previous two weeks, most of the lectures were not relevant to the lab work. Because of this, the academic and challenge goals of the week are noticeably disjoint.

The lectures during week three focused on localization and mapping. The goal was to understand common algorithms that are used to let a robot know where it is in its environment and can be used to plan paths to specific goals.

The weekly challenge did not required groups to implement any localization or mapping functionality. The cars had to drive around for two minutes in an enclosed pen, avoid hitting any obstacles, and identify as many different colored blobs as possible.

##Approach

###SLAM Algorithm



###Potential Fields



###Challenge Approach 

My team decided to use two nodes for the weekly challenge. One would control the cars motion and implement a potential field algorithm. The other would detect and record images of blobs that the car's camera captured. These nodes were completely independent of each other and did not communicate at all. We decided to have two independent nodes because it was not necessary for them to communicate. This week, we focused on perfecting the simplest algorithms that could accomplish our goals. 



##Process

###Explorer Node

The potential field algorithm was surprisingly simple to implement. We wrote the first draft of the code all together on codeshare.io, and it took us less than half an hour. Other than a few syntax errors, the code was functional right off the bat and just needed tweaking. 



###Blob Search

EXPLAIN BASIC PROCESS
The blob detection node would look for contours of all four colors and determine the size of the largest of each color. If this size was larger than a predetermined threshold size (INSERT), 

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

Figure BLANK: Successful detection of blob (10 pts)

![Failure](https://cloud.githubusercontent.com/assets/18174572/17710383/00560a02-63bb-11e6-9a59-b3463de206e9.png)

Figure BLANK + 1: Detection of background as a blob

![Different Failure](https://cloud.githubusercontent.com/assets/18174572/17710379/00388d74-63bb-11e6-8739-9a6b26836600.png)

Figure BLANK + 2: Correct detection of green blob and incorrect detection of red blob

From the pictures it was clear that our car could have been more successful at blob detection if we had set the speed to be slightly lower. The images were blurred, which most likely did nothing to help the image processing. The car definitely went faster than necessary as it made at least five full loops around the course in the allotted two minutes. Clearer images could have led to more accurately identified blobs.

##Sources

(1)
