#**Week One: Technical Work**

##**Goals**

  The first week of the program served as a period to set the foundation of ROS, Linux, and Python
  knowledge, as well as acquaint students with the RACECAR platform. Everyone started at a slightly
  different level (some students had prior Python experience, everyone got through different amounts
  of the pre-program coursework), and for the first few days of week one the instructors were
  primarily concerned with getting all students on a level that would allow them to succeed in the
  weeks to follow.

  In week one groups also were given the task of programming their RACECARs to wall follow -- or,
  drive forward and stay a specific distance away from a wall -- for ~30 feet as quickly as possible.
  The cars had to be able to follow both the left and right walls and switch between the two on
  command. Since all of the cars had the same speed cap (2 meters per second), the only way
  for teams to differentiate themselves was by having a better algorithm (in terms of computation
  time and oscillation levels).

##**Approach**

###The RACECAR

In order for groups to control their RACECARs, it was first crucial for them to understand them and all of their components.
![RACECAR](https://cloud.githubusercontent.com/assets/18174572/17645837/ae61aabe-617e-11e6-96b2-f528a82376e1.png)
Figure 1: Labeled illustration of the RACECAR used in this course (1); note that the cars used in the Beaver Works Summer Program did not have active stereo cameras, and the passive cameras were mounted above the LiDAR where the active camera appears in this image.

The robots used in this program were equipped with an advanced supercomputer and sensors that provided the data necessary for the algorithms to work. (1)
  * **Chassis:** The basic frame of the vehicle is the Traxxas Rally 74076, a 1/10 scale RC car with four wheel drive and    Ackermann front wheel steering. It is capable of speeds up to 40 miles per hour, but this program's purposes this to 2 m/s (or 4.5 mph).
  * **Processor:** The computer aboard the car is the Nvidia Jetson TX1 embedded systems module running Ubuntu for ARM. It is equipped with 256 CUDA cores that deliver over 1 TeraFLOPs of performance (2). The large number of GPU cores allows the TX1 to perform many parallel operations at the same time, making it extremely fast and efficient. The speed definitely comes in handy for the RACECAR's purposes; data could be processed and commands could be given in real time, which is very important for the reactive navigation the cars did for the vast majority of the time.
  * **2D LiDAR:** Each car also had a 2D Hokuyo UST 10LX scanning laser rangefinder. The LiDAR has a range of .06m to ~10m and an accuracy of +/-40mm. It has a scan angle of 270 degrees and a speed of 40Hz. The laser scanner was one of the most frequently used scanners throughout the duration of the program. It scans 270 degrees and splits it into 1081 points, returning a list of the distances (in meters) from the car that each of the points are. Specifically, it does this by sending out beams of light (lasers) and measuring the time it takes for them to come back. The following formula:

                                        D = ct/2                                                    (eq. 1)

Where c = speed of light and t = time, can then be used to determine the distance (D). This data was vital as most steering decisions the car made (all of them during week one) were based upon it.

![Hokuyo](https://cloud.githubusercontent.com/assets/18174572/17646411/ba69fbc4-6195-11e6-8ebb-77e65e6b56e5.png)

Figure 2: Hokuyo LiDAR and diagram depicting its range (1)
  * **IMU:** A Sparkfun 9 Degrees of Freedom "Razor" Inertial Measurment Unit was also present on each vehicle. The IMU has three sensors: a MEMS (MicroElectroMechanical System) three-axis accelerometer that assesses translational acceleration, a MEMS three-axis gyroscope that measures Coriolis force, and a three-axis Anisotropic MagnetoResisteance (AMR) magnetometer. The IMU is used to compute the current acceleration of the car.
  * **Passive Stereo Camera:** Unlike the diagram pictured above, the cars utilized during the Beaver Works program had only one camera: a Sensorlabs ZED Passive Stereo Camera with automatic depth perception from .7 to 20 meters and a field of view of 110 degrees. Although groups never utilized the depth perception functionality of the camera, it is made possible because the camera actually consisted of two separate cameras that would record the same image, use image processing software to identify matching points in the images, and then solve the translation between them to obtain depth data. The farther apart an object seems to the two cameras, the closer it is.

![Car and Controller](https://cloud.githubusercontent.com/assets/18174572/17651127/cbe4150e-622d-11e6-96c7-6885b09627ee.png)

Figure 3: RACECAR and remote controller (1)

In addition, cars came with a controller (see above) that could be used to command the car's movements. Before ever running a program, the controller would be connected to the car. The left trigger worked as a "deadman switch" which would immediately stop the car upon being pressed. This was a safety measure taken to protect the RACECARs. A human was always in control and could stop the car from colliding with an obstacle if a program did not run as planned.

###Basics of ROS

Students also had to have a basic understanding of the Robot Operating System (ROS) in order to complete any of the assigned tasks.

ROS is an operating system that is used for robots. The overarching goal of the system is to support code reuse in robotics; before ROS, people had to start from scratch whenever they wanted to program a new robot, even though a lot of the code that they wrote had already written before (4). Because ROS is open source, meaning all source code is made available, ROS saves software developers a huge amount of time because they can reuse code written by others. This allows progress in robotics to be made much more quickly. ROS is a powerful, flexible (supports multiple languages and multi-machine systems) tool that is widely used in academia and industry and is supported by the Open Source Robotics Foundation (OSRF). (5)

One aspect of ROS that makes it so effective for robotics software development is how its design supports modularity. Most tasks that robots have to accomplish are complex and have many different components. Completing each component linearly is time consuming and does not take advantage of the Jetson TX1's many GPU cores. Luckily, ROS makes it very simple to employ a modular software design by allowing elaborate tasks to be broken into simpler pieces. Then, multiple parts of the problem can be solved at the same time, allowing programs to run much more quickly. (5)

ROS utilizes modularity by organizing programs into nodes. Nodes are processes performing specific computations in the ROS system. There can be as few as one and as many as one hundred in a single program. The nodes have to be able to communicate with each other, and they do that using messages and topics. Messages are strictly typed packets of data sent between ROS nodes. They are sent over topics: unidirectional communication links between ROS nodes. When a node wants to send data, it must **publish** a message to a specific topic, and the node that wants to receive that data must **subscribe** to that topic. Each topic is linked to a single message type. It is important to note that one or more nodes may publish messages to a topic and one or more nodes can subscribe to any topic. In addition, an individual node can publish or subscribe to as many topics as it needs to. The ROS Master process is responsible for linking nodes together. It coordinates the peer-to-peer communication links between nodes. Nodes that wish to publish advertise to the ROS Master on the desired topic. Nodes that wish to subscribe to that topic tell the ROS Master, and it establishes a connection between the two nodes. (5)


###Control Systems
To help us with this first challenge, a robotics software engineer from NASA's Jet Propulsion Laboratory (JPL), Kyle Edelberg, gave technical lectures on control systems that we could use.

A simple definition of a control system is something that takes a system (specifically the RACECAR for the program's purposes) from state A to state B, the desired state. The controller is implemented in the software as the program(s) that tell the system what to do, and the system is the hardware (the RACECAR for Beaver Works' purposes). (6)

There are two basic types of control that a system can use: open loop control and closed loop control. (6)

Open loop control is the more primitive of the two types of control system. The controller tells the system to do something and receives no feedback to let it know how close it is to completing the task. An example of open loop control is if a RACECAR had to move 10m and the top speed was 2m/s, so the program told the car to run at full speed forward for five seconds. The car would run for the five seconds and stop, but the controller would have no idea if it was successful. In addition, this method does not account for many errors such as the wheels sticking, slipping, or being misaligned, and if any of that happened, the program would not be able to adjust and achieve the desired state. Open loop control is not usually used, but sometimes when the reaction time for the controller to adjust its plan would be too slow anyway or during testing it is used. (6)

Closed loop control is usually preferred over open loop. In this control method, the controller receives feedback from the system to help it achieve the desired value. Closed loop control is what groups used for their wall following algorithms. (6)

![Open Loop Control (Wall Follow)](https://cloud.githubusercontent.com/assets/18174572/17651717/ff97b6e6-623a-11e6-8448-2cbcaff08204.png)

Figure 3: Diagram depicting closed loop control for wall following (6)

The above diagram illustrates how closed loop control works for wall following. A desired distance (Ddes) is inputed into the controller as well as the current distance(D) from the wall, which the system's sensors send to the controller. The controller then subtracts the current distance from the desired distance to obtain the error, which the system wants to  be as close to zero as possible. Based on the error, the controller sends steering commands to the system, which sends more data back to the controller in a continuous loop. (6)

Mr. Edelburg introduced us to two types of closed loop control that could be used: bang bang control and PID control.

Bang bang control is the simplest form of closed loop control. It looks at the error value (Ddes - D). If it's positive, the car is too close to the wall, so the controller tells the car to steer as far as possible away from the wall (if following the right wall, the steer command would be -1, which is a full left). If the error value is negative, the car is too far away from the wall so the program tells the car to steer all the way towards the wall (again, in a right wall following scenario the command would be 1, full right). Bang bang control is effective, but causes significant oscillations in the car's forward motion. This means the car is traveling farther than if it were able to drive straight, which is not ideal when teams wanted their cars to move as quickly as possible. (6)

PID control, or, Proportional Integral Derivative control, is another fairly simple control scheme that makes use of the following equation (6):

                              u = kp*e + ki*∫e + kd*ẻ                                               (eq. 2)

Where u is the steering command (a number between -1 and 1, or, full left and full right), kp, ki, and kd are experimentally determined constants, e is the error, ∫e is the summation of the errors (integral with respect to time), and ẻ is the derivative of the errors. Each of the terms of this equation has a specific goal. The kp term initially brings the error value close to zero, the ki term drives it all the way down, and the kd value helps with stability, i.e., minimizes oscillations (6). Most groups opted to use PID control in week one's final challenge.

![PID](https://camo.githubusercontent.com/bbede27c5fa69f4764cf2727cb42740aa7d46b5b/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f332f33332f5049445f436f6d70656e736174696f6e5f416e696d617465642e676966)

Figure 4: Animation showing the effects of changing PID values (3)

###Challenge Approach

After gaining the necessary background through lectures and short labs, groups were ready to start working on the implementation of a wall following node. When deciding our approach, my team prioritized learning and obtaining experience with the robot above all else, which is reflected in all of the choices that were made.

In order to get more practice writing nodes, my group decided to first write one that used the bang bang control system and then write a PID node. Although this approach left less time to tweak PID values to perfection, my team decided it was worth it in the long run to have a better understanding of nodes and ROS in a general sense.

Another decision our group made going into week one's challenge was to not delegate tasks; for the most part we all worked on everything together. Again, working as a full group was not the most efficient way to go about the task, but it made it much easier to ensure that all group members understood what was going on throughout the whole process.

The final decision the group had to make before starting to code was how to interpret the laser data. This at first seems like a straightforward problem; find the point on the scan that is at a 90 degree angle with the front of the car and use that distance as th distance from the wall. However, with the car steering and very rarely driving exactly parallel to the wall, this would not always be the correct distance. The car would sometimes be much closer to the wall than that single point would appear. To combat this there were two options. The first was to use trigonometry by taking two points at a 30 degree angle and using law of sines and law of cosines to solve for the actually distance from the wall. The second was to take a large swathe of points and find the one with the smallest value. This would be the minimum distance between the car and the wall. Our group chose to go with the second approach because it was simpler to program and did not make use of computationally expensive trigonometric functions. In addition it was more reliable than relying on just two points; if the car reached a corner, the point farther out in front could get an extremely high value that would cause the calculated distance to be incorrect. By looking at the smallest value within a range, the chance of being thrown by massive outliers is virtually eliminated.

##**Process**

The process of implementing a wall follow algorithm was cyclical. Our team would write code, test it to see what it would do, change the code, and retest. To get started we used node templates found on the ROS wiki. This gave us a good idea of the format we needed to use and then we just filled it in with our own code. There were a few bumps along the way as this was our first time writing a node but we worked methodically through everything and made sure to thoroughly comment the code to make it understandable.

The bang bang controller followed solely the left wall and had a scan range of 540 to 930. The node 'wall_bang' subscribed to the 'scan' topic to obtain the LiDAR data and published drive commands to the '/vesc/ackermann_cmd_mux/input/navigation' topic. Once the code was functional, it required very little testing because there were no values to tweak. The one thing we added on top of basic bang bang control was a threshold value; if the error was small enough (specifically, if the absolute value of the error was less than .03 meters), the node will publish a steering command of zero, which tells the car to go straight. The bang bang controller was functional but oscillated a lot.

After successfully coding the bang bang controller, we moved on to PID. One thing we decided during the coding process was to turn PID control into PD control; the I term is just serves to bring the error value closer to zero, and in our case, that was not important. The car just had to follow a wall as quickly as possible; the exact distance it was from the wall, which is the only thing that implementing the I portion of PID control would change, did not matter. By scratching it we saved computational time and had more time to test PD values.

Writing the PD node did not take that long because we just had to alter and add a few things in the bang bang algorithm.  We completed the process in steps. First, we just had a P value. Then, once we had tested that and made sure that part was functional, we added in the derivative element. Breaking the code down into testable parts makes the debugging process much more efficient because the sources of errors are easier to locate. Of course, once the D section was added in, the kp value had to be altered. Our group spent a lot of our lab time testing different kp and kd values to optimize the algorithm. On Kyle Edelberg's recommendation, we started with the kp value very low and gradually incremented it, then did the same with kd. The values we settled on were .7 for kp and .6 for kd.

This algorithm could follow either the left or the right wall depending on what button was pressed on the controller. The 'a' button made it follow the left wall and 'b' made it follow the right. If no buttons were pressed, it would default to following the right wall. For our scan ranges, we used 200 to 540 to for the right and 540 to 900 for the left.

Another feature we added to this node was a 'safety.' We took a small scan directly in front of the robot (from 525 to 555), and if the minimum distance to a point within that range was less than .5 meters, the speed of the robot would be set to -.1. We used -.1 instead of 0 to make the robot stop more quickly. Although the safety could have been implemented in its own node, it seemed simpler to us to just make it part of the wall following node to avoid dealing  with node hierarchy.

Full code for both algorithms can be found in the scripts folder of this github page.

##**Results**

  The final challenge was set up as a "drag race." In the first round, cars had to complete two time
  trials: one following the left wall and one following the right. Each car's fastest time was used
  to place them in the second round. The fastest car got a bye to the next round, and the rest of the
  nine cars were paired off and raced head to head. The races were best two out of three and the
  fastest of each of these pairings moved on to the final round, as well as the fastest losing car
  from all the rounds. In the final round three pairs of cars again raced best two out of three, this
  time vying for gold, silver, and bronze medals.

  In the time trials, car 45, my group's car, came in fourth with a time of 8.645 seconds. In round
  two, we were up against car 34, which did not complete any successful runs in the three attempts,
  so we advanced to the final round. In the final round the start was slightly different from in the
  time trials; in the time trials, the timer would start as soon as the car moved across the start
  line, but in the finals it would start as soon as the start signal was given. The cars take time
  to get started, so this change was reflected in the final results. Our best time was 9.58 seconds,
  almost a full second slower than in the time trials. We placed sixth overall in the final round.
