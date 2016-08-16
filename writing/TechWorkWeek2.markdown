#Week Two: Technical Work

##Goals
  
After week one, students felt more comfortable with the cars and basic motion commands. So, for week two, groups built upon these skills by combining them with basic computer vision.

Like the previous week, there were two main goals during the week. The first was to  learn about image processing and become comfortable using OpenCV, an open source computer vision software library (1). The final challenge goal incorporated things learned during both weeks. The cars had to be able to detect a brightly colored piece of construction paper, or, 'blob', and drive toward it using visual servoing. This blob was either red or green, and once the robot got a certain distance away from it (approximately one meter), it had to make a decision based upon this color. If the blob was green, the car had to turn right and follow the left wall to a finish line. If it was red, the car had to turn left and follow the right wall to a different finish line. Again, teams were to complete these tasks as quickly as possible.

##Approach 
  
##Process
  
##Results

For week two's challenge, each car had three opportunities to complete the tasks. For each of these three tries, the blob color would be randomly chosen as would the starting orientation of the car. The blob would be either red or green and the car would either start pointing directly at the blob or be slightly rotated to the left or right. The time (if there was one) would be recorded for each run and the single best time would be used to rank the cars at the end.

For our first run, our car was assigned the green blob and was rotated slightly to the right. For the second run, we again were given the green blob but our car was not rotated. In the final run we had to detect a red blob and we started rotated to the right again. We were one of the seven teams that did not complete any runs successfully. This was unsurprising considering we only had one successful test run, but disappointing nonetheless. 

During the first and third runs, our car made it into the visual servoing box and turned in the correct direction, but just continued to turn in a circle and did not make it to the finish line. The car's most successful attempt was its second (green no rotation), where it made it into the box, made the correct turn (right), wall followed the left wall for a little while, but about three meters away from the finish line suddenly turned right and collided with the wall on the other side. There are many possible reasons for the car's malfunctions. It could have been something as simple as a sign error in the left and right steer values or something that would take more time to debug, like a faulty turn command. Given more time our team may have made some very different choices, such as splitting the visual servoing and wall following into two separate nodes instead of combining them into one. This week was difficult, but groups were able to accomplish the first goal, gaining experience with image processing, which would help them in the weeks to follow. 

##Sources

Cited

(1) http://opencv.org/about.html
