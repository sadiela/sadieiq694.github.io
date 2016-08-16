#Week Two: Technical Work

##Goals

After week one, students felt more comfortable with the cars and basic motion commands. So, for week two, groups built upon these skills by combining them with basic computer vision.

Like the previous week, there were two main goals during the week. The first was to  learn about image processing and become comfortable using OpenCV, an open source computer vision software library (1). The final challenge goal incorporated things learned during both weeks. The cars had to be able to detect a brightly colored piece of construction paper, or, 'blob', and drive toward it using visual servoing. This blob was either red or green, and once the robot got a certain distance away from it (approximately one meter), it had to make a decision based upon this color. If the blob was green, the car had to turn right and follow the left wall to a finish line. If it was red, the car had to turn left and follow the right wall to a different finish line. Again, teams were to complete these tasks as quickly as possible.

##Approach

Again, some background knowledge is necessary before my group's approach can be described.

###Computer Representation of Images

A computer deals with color images as 2D pixel arrays where each pixel encodes a color. There are several ways in which computers can represent colors, but in the Beaver Works course students mostly worked with RGB and HSV formats.

The human eye perceives color using specialized cells called cones. There are three different types of cones in our eyes that all respond most strongly to different wavelengths of light; red, green, or blue. RGB representation is based off the human visual system. Each pixel in the 2D array that represents an image encodes a color with the triplet (R, G, B). Because color pixels are typically encoded in 24 bits, or, 8 bits per color, the R, G, and B components take values between 0 and 255. (0, 0, 0) encodes black, (255, 255, 255) encodes white, and any triplet in which all three values are the same represents gray. (255, 0, 0) would be a 'perfect' red.

An alternative to RGB is the HSV color model. This system also uses triplets to represent colors, but the three values represent hue, saturation, and value. Hue is an angle out of 180 degrees. 0 degrees is red, 60 degrees is green, and 120 degrees is blue. Saturation is out of 255 and represents the intensity of the color. Value is also on a scale of 0 to 255 and is a measure of the brightness of a color.

![HSV Chart] (https://cloud.githubusercontent.com/assets/18174572/17703787/f45c870e-63a0-11e6-86b2-d12b2cd06902.png)

Figure 1: Diagram showing how colors change in accordance with HSV values

The HSV model works better for blob detection because it is much more robust under illumination changes.

###Intro To OpenCV Tools



###Challenge Approach


  
##Process

##Results

For week two's challenge, each car had three opportunities to complete the tasks. For each of these three tries, the blob color would be randomly chosen as would the starting orientation of the car. The blob would be either red or green and the car would either start pointing directly at the blob or be slightly rotated to the left or right. The time (if there was one) would be recorded for each run and the single best time would be used to rank the cars at the end.

For our first run, our car was assigned the green blob and was rotated slightly to the right. For the second run, we again were given the green blob but our car was not rotated. In the final run we had to detect a red blob and we started rotated to the right again. We were one of the seven teams that did not complete any runs successfully. This was unsurprising considering we only had one successful test run, but disappointing nonetheless.

During the first and third runs, our car made it into the visual servoing box and turned in the correct direction, but just continued to turn in a circle and did not make it to the finish line. The car's most successful attempt was its second (green no rotation), where it made it into the box, made the correct turn (right), wall followed the left wall for a little while, but about three meters away from the finish line suddenly turned right and collided with the wall on the other side. There are many possible reasons for the car's malfunctions. It could have been something as simple as a sign error in the left and right steer values or something that would take more time to debug, like a faulty turn command. Given more time our team may have made some very different choices, such as splitting the visual servoing and wall following into two separate nodes instead of combining them into one. This week was difficult, but groups were able to accomplish the first goal, gaining experience with image processing, which would help them in the weeks to follow.

##Sources

Cited

(1) http://opencv.org/about.html

(2) Detry, Renaud. (2016) Image Processing [Powerpoint slides]. Retrieved from https://piazza-resources.s3.amazonaws.com/ikimc42bcsv68r/iqv1h3yfxfl3jp/11imageprocessingcv.pdf?AWSAccessKeyId=AKIAIEDNRLJ4AZKBW6HA&Expires=1471369483&Signature=o4VdJxFZKf5dYsmyXqz2MLrHVAE%3D

(3) http://www.livescience.com/32559-why-do-we-see-in-color.html
