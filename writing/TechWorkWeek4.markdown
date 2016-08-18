# Technical Work: Week Four

##Goals

The goal of the final week was for students to bring together everything they had learned and showcase it at Walker Memorial Hall on Friday, August 5. The exhibition consisted of three main sections: two technical challenges and the mini grand prix.

The first tech challenge was the same as the third week's challenge; Cars had to explore autonomously and avoid obstacles while recognizing and recording different colored blobs. 

The second tech challenge was somewhat similar to week two's challenge. The cars were required to detect a blob and based on its color turn either left or right. This is different from the original week two challenge because the cars were not required to use visual servoing and did not have to wall follow. The challenge was altered in this way so that code from it could be reused for the mini grand prix (see details below). 

The mini grand prix consisted of time trials (three attempts per car) with the cars alone on the track, three heat races in which three cars would race each other, and a final grand prix with all nine cars on the track.

##Approach

Our plan going into week four was to direct most of our energy towards the time trials and grand prix race. We already had functional code for the first technical challenge and a solid start on code for the second one, so the grand prix was what we had to do the most work on and where we dedicated most of our time. 



##Process

Our carefully planned approach to each component of the final challenge was not strictly followed. Our group faced a variety of setbacks diring the week that caused us to change our plans very frequently.

- switched between several different plans
- wall follow for time trials, didnt work out
- originally wanted largest open space for grand prix
- ended up using potential field for both races
- extremely slow connection; had to walk around with ethernet cord
- zed camera malfunctions
- had to use instructors car because our servo overheated and broke

During the first technical challenge, another vehicle collided with the side of our car (car 7) and our servo (the steering mechanism on the car) overheated. The combination of these events led to the servo dying; car 7 could no longer turn its wheels. 
We had to use the instructor's car in 


##Results

### Technical Challenge 1: Exploring Space

The exploring challenge was exactly the same as week three's challenge; the cars just had to drive around an enclosure autonomously, detect blobs, and avoid obstacles. Our car was successful in this challenge. Later several cars were placed in the pen together and our car still managed to avoid all collisions. 

https://www.youtube.com/watch?v=TqN69NZ3m8w&feature=youtu.be

Figure 1: Robot Exploring Space and Avoiding Obstacles

### Technical Challenge 2: Making the Correct Turn

The second technical challenge was a slightly simplified version of week two's final challenge. The cars had to drive up to a fork in the racetrack, detect a blob, and decide which direction to turn based on its color.

Because of the ZED camera malfunctions and how slow all image-related programs were running on our car, my team did not manage to perfect the code for the second technical challenge and were unable to participate. We did get very close to a functional algorithm, and had we been able to test and debug for a longer period of time, our robot most likely would have been able to complete the challenge. 

### Time Trials

In the time trials, cars had three attempts to go around the race track as quickly as possible. Cars were first ranked by number of successful runs, then by time. On one of the attempts, a shortcut would be opened, signified by the red blob above the shortcut entrance being changed to green. If a car could successfully take the shortcut, it would have a significantly faster time, but if it took it when it was not open, the car would not receive a time for that run. 

![racetrack](https://cloud.githubusercontent.com/assets/18174572/17789577/d61cab9a-6560-11e6-86b3-74ce04737ddb.png)

Figure 2: Map of Grand Prix Racetrack. Cars Moved counterclockwise around the course.

Because of all of the hardware troubles we encountered, my group decided to not bother with the shortcut and go around the full course for all three runs.

Table 1: Time Trial Results

|Lap 1|Lap 2|Lap 3|Best Time|
|-----|-----|-----|---------|
|35.61 |35.63 |35.33 |**35.33** |

Our fastest lap took the car 35.33 seconds, which earned us third place overall. The time trial results were used to seed cars into rows for the grand prix; first, second, and third place would be in the first row, fourth fifth and sixth in the second, and seventh, eighth, and ninth in the third. 

### Heat Race and Grand Prix

After the time trials, groups of three cars raced together to vie for the most advantageous spot in the row. First place in the heat would be on the left, second in the center, and third on the right. Our car was in the first heat with cars 34 and 63 and got second place.

In the final grand prix, all nine cars raced the course at the same time. Our car had a rough start and was passed by several cars behind it, but managed to make up a lot of ground during the lap and finished fourth overall.
