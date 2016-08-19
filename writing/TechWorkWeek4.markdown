# Technical Work: Week Four

##Goals

The goal of the final week was for students to bring together everything they had learned and showcase it at Walker Memorial Hall on Friday, August 5. The exhibition consisted of three main sections: two technical challenges and the mini grand prix.

The first tech challenge was the same as the third week's challenge; Cars had to explore autonomously and avoid obstacles while recognizing and recording different colored blobs. 

The second tech challenge was somewhat similar to week two's challenge. The cars were required to detect a blob and based on its color turn either left or right. This is different from the original week two challenge because the cars were not required to use visual servoing and did not have to wall follow. The challenge was altered in this way so that code from it could be reused for the mini grand prix (see details below). 

The first part of the mini grand prix consisted of time trials (three attempts per car) with the cars alone on the track. On one of the attempts, a shortcut would be opened, signified by the red blob above the shortcut entrance being changed to green. If a car could successfully take the shortcut, it would have a significantly faster time, but if it took it when it was not open, the car would not receive a time for that run.

Aftr the time trials there were three heat races in which three cars would race each other, and a final grand prix with all nine cars on the track. For both of these events the entrance to the short cut was entirely blocked off.

##Approach

Our plan going into week four was to direct most of our energy towards the time trials and grand prix race. We already had functional code for the first technical challenge, and, as previously mentioned, it was not necessary to spend time on the second technical challenge as code from the grand prix could be reused for it. The grand prix was what we had to do the most work on and where we dedicated most of our time.  We planned to have two separate programs. One for the time trials and one for the heat races and grand prix.

For the time trials we planned to implement a wall following node. This made sense because the goal was to go as fast as possible. Since there were no obstacles, it would be fastest to hug the inside wall to minimize the distance the car needed to travel. The shortcut was the on the left side of the track, so on the shortcut run the car could just hug the left wall for the entire duration of the lap. However, when the blob above the shortcut was red, the car would need to go down the right fork. To implement this, we planned to only look for red blobs larger than a certain size. If one was detected, the car would switch to following the right wall for 10 seconds and then switch back to the left.

For the grand prix we wanted to use a 'greatest open space' algorithm. This method takes a laser scan and compares each of the distances to a threshold value (e.g. two meters). If the point is farther than that distance away from the car, it is marked as free space. The algorithm then looks for the greatest group of free points clumped together and steers the car in the direction of it. The greatest open space algorithm was preferable to both wall following and potential fields. This is because in the grand prix the robots had to deal with multiple moving obstacles. The wall following node only scans one side of the track and would be completely oblivious to potential collisions on its other side, and a potential field algorithm would drive the car backward any time it got close to another robot, making it virtually impossible to pass. With greatest free space the car would be aware of its entire surroundings and would not back up when it encountered another car.

##Process

###Race Preparation

Our carefully planned approach to each component of the final challenge was not strictly followed, which definitely held us back throughout the week. When something was not working, we frantically jumped to a different plan, and if that did not work out either we would switch back. We should have put all of our effort into one program instead of wasting time on several programs that we did not even end up using.

In addition to poor decision making, we had several problems with our car's hardware. The ZED camera malfunctioned on multiple occasions and cost us a lot of time. In addition, every time the car ran any form of vision code, the programs would run extremely slowly and sometimes shut down. We had to connect a computer to it with an ethernet cord whenever we needed to test the car, which was difficult.

Eventually because of all the issues surrounding blob detection and the time restraints we were under, our team reevaluated and made a new, much simpler plan. We decided to scratch all code concerning blob detection and use the same code for the time trials and the grand prix. Instead of 'greatest open space,' a potential field algorithm would be implemented. Even though this was not our first choice, we had a very good potential field algorithm from the previous week that just needed to be slightly adjusted for the grand prix challenge. 

The major adjustment we made to the potential field algorithm was add an artificial charge pushing it slightly to the right. This made sure that the car would turn right every time it got to the  fork in the racetrack. In addition we vamped up the propelling charge from three to five and the Alaser from .005 to .01. These were the only changes we made to the algorithm.

###Race Day

During the first technical challenge, another vehicle collided with the side of our car (car 7) and our servo (the steering mechanism on the car) overheated. The combination of these events led to the servo dying; car 7 could no longer turn its wheels. So, an hour before the beginning of the time trials, we had to switch cars and use the instructor's. Because our algorithm had been calibrated for our original car, car 7, we were given permission to test on the race track and make necessary adjustments to our code.

##Results

### Technical Challenge 1: Exploring Space

The exploring challenge was exactly the same as week three's challenge; the cars just had to drive around an enclosure autonomously, detect blobs, and avoid obstacles. Our car was successful in this challenge. Later several cars were placed in the pen together and our car still managed to avoid all collisions. 

https://www.youtube.com/watch?v=TqN69NZ3m8w&feature=youtu.be

<iframe width="560" height="315" src="https://www.youtube.com/embed/TqN69NZ3m8w" frameborder="0" allowfullscreen></iframe>

Figure 1: Robot Exploring Space and Avoiding Obstacles

### Technical Challenge 2: Making the Correct Turn

The second technical challenge was a slightly simplified version of week two's final challenge. The cars had to drive up to a fork in the racetrack, detect a blob, and decide which direction to turn based on its color.

Because of the ZED camera malfunctions and how slow all image-related programs were running on our car, my team did not manage to perfect the code for the second technical challenge and were unable to participate. We did get very close to a functional algorithm, and had we been able to test and debug for a longer period of time, our robot most likely would have been able to complete the challenge. 

### Time Trials

The time trials were the first challenge we had to complete with the new car. During the time trials, cars had three attempts to go around the race track as quickly as possible. Cars were first ranked by number of successful runs, then by time. 

![racetrack](https://cloud.githubusercontent.com/assets/18174572/17789577/d61cab9a-6560-11e6-86b3-74ce04737ddb.png)

Figure 2: Map of Grand Prix Racetrack. Cars Moved counterclockwise around the course.

Because we opted to ignore the shortcut and go the long way for each run, all of our times were within three tenths of a second.

Table 1: Time Trial Results

|Lap 1|Lap 2|Lap 3|Best Time|
|-----|-----|-----|---------|
|35.61 |35.63 |35.33 |**35.33** |

Our fastest lap took the car 35.33 seconds, which earned us third place overall. The time trial results were used to seed cars into rows for the grand prix; first, second, and third place would be in the first row, fourth fifth and sixth in the second, and seventh, eighth, and ninth in the third. 

### Heat Race and Grand Prix

After the time trials, groups of three cars raced together to vie for the most advantageous spot in the row. First place in the heat would be on the left, second in the center, and third on the right. Our car was in the first heat with cars 34 and 63 and got second place.

In the final grand prix, all nine cars raced the course at the same time. Our car had a rough start and was passed by several cars behind it, but managed to make up a lot of ground during the lap and finished fourth overall, narrowly beating out car 4.

Overall, we could have been more successful had we stuck to our original plan, but our car performed well and we were proud of the results we acheived.
