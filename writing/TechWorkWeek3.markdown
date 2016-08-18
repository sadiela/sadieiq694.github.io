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

| Color | Hue Min | Hue Max | Saturation Min | Saturation Max | Value Min | Value Max |
|-------|:-------:|:--------:|:--------------:|:-------------:|:--------:|:----------:|
|Red    |    0     |    15      |                |      1      |            |     1       |
|Green    |         |          |                |     1       |            |     1       |
|Yellow   |         |          |                |     1       |            |    1        |
|Blue    |         |          |                |      1      |            |     1       |

##Results

EXPLAIN POINT SYSTEM

In the final challenge, car 7, my group's car, detected 6 blobs and had just one collision, which ended us with a total score of 58 points. My team received second place overall for this performance.

![sucess](https://cloud.githubusercontent.com/assets/18174572/17710382/00521852-63bb-11e6-83a6-6a10a6911656.png)

Figure BLANK: Successful detection of blob (10 pts)

![Failure](https://cloud.githubusercontent.com/assets/18174572/17710383/00560a02-63bb-11e6-9a59-b3463de206e9.png)

Figure BLANK + 1: Incorrect detection of blob

##Sources
