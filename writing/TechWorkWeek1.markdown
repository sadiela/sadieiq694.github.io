#Week One: Technical Work


## Goals:

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

##**Approach:**
  
###The RACECAR
      
In order for groups to control their RACECARs, it was first crucial for them to understand them and all of their components. 
![RACECAR](https://cloud.githubusercontent.com/assets/18174572/17645837/ae61aabe-617e-11e6-96b2-f528a82376e1.png)
Figure 1: Labeled illustration of the RACECAR used in this course (1); note that the cars used in the Beaver Works Summer Program did not have passive stereo cameras

The robots used in this program were equipped with an advanced supercomputer and sensors that provided the data necessary for the algorithms to work. 
  * **Chassis:** The basic frame of the vehicle is the Traxxas Rally 74076, a 1/10 scale RC car with four wheel drive and    Ackermann front wheel steering. It is capable of speeds up to 40 miles per hour, but this program's purposes this to 2 m/s (or 4.5 mph).
  * **Processor:** The computer aboard the car is the Nvidia Jetson TX1 embedded systems module running Ubuntu for ARM. It is equipped with 256 CUDA cores that deliver over 1 TeraFLOPs of performance (2). The large number of GPU cores allows the TX1 to perform many parallel operations at the same time, making it extremely fast and efficient. The speed definitely comes in handy for the RACECAR's purposes; data could be processed and commands could be given in real time, which is very important for the reactive navigation the cars did for the vast majority of the time. 
  * **2D LiDAR:** Each car also had a 2D Hokuyo UST 10LX scanning laser rangefinder. The LiDAR has a range of .06m to ~10m and an accuracy of +/-40mm. It has a scan angle of 270 degrees and a speed of 40Hz. The laser scanner was one of the most frequently used scanners througout the duration of the program. It scans 270 degrees and splits it into 1081 points, returning a list of the distances (in meters) from the car that each of the points are. Specifically, it does this by sending out beams of light (lasers) and measuring the time it takes for them to come back. The following formula:

                                            D = ct/2                                                    (eq. 1)

Where c = speed of light and t = time, can then be used to determine the distance (D). This data was vital as most steering decisions the car made (all of them during week one) were based upon it. 
 
![Hokuyo](https://cloud.githubusercontent.com/assets/18174572/17646411/ba69fbc4-6195-11e6-8ebb-77e65e6b56e5.png)

Figure 2: Hokuyo LiDAR and diagram depicting its range (1)
  * **IMU:** A Sparkfun 9 Degrees of Freedom "Razor" Inertial Measurment Unit was also present on each vehicle. The IMU has three sensors: a MEMS (MicroElectroMechanical System) three-axis accelerometer that assesses translational acceleration, a MEMS three-axis gyroscope that measures Coriolis force, and a three-axis Anisotropic MagnetoResisteance (AMR) magnetometer. The IMU is used to compute the current acceleration of the car.
  * **Passive Stereo Camera:** Unlike the diagram pictured above, the cars utilized during the Beaver Works program had only one camera: a Sensorlabs ZED Passive Stereo Camera with automatic depth perception from .7 to 20 meters and a field of view of 110 degrees. Although groups never utilized the depth perception functionality of the camera, it is made possible because the camera actually consisted of two separate cameras that would record the same image, use image processing software to identify matching points in the images, and then solve the translation between them to obtain depth data. The farther apart an object seems to the two cameras, the closer it is. 

Each car CONTROLLER 
  

###Basics of ROS

Students also had to have a basic understanding of the Robot Operating System in order to complete any of the assigned tasks.

ROS is 
 
  
###Control Systems
To help us with this first challenge, a robotics software engineer from NASA's Jet Propulsion Laboratory (JPL), Kyle Edelberg, gave technical lectures on control systems that we could use.

###Challenge Approach

After gaining the necessary background through lectures and short labs, groups were ready to start working on the implementation of a wall following node. In order to get more practice writing nodes, my group decided to first write one that used the bang bang control system and then write a PID node. 

##**Process:**
  
  My group decided to first implement bang-bang control, and then once we got that working, move on 
  to PID. 

##**Results:**
  
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
  almost a full second slower than in the time trials. 

Sources 
(1) Guldner, Owen. (2016) Introduction to the RACECAR Platform [Powerpoint slides]. Retrieved from https://drive.google.com/file/d/0B6jv7Ea8ZHnNZmZTbUdLWktyLW8/view
(2) http://www.nvidia.com/object/jetson-tx1-module.html
