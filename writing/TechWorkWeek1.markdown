Week One: Technical Work
========================


  Goals:
  
  The first week of the program served as a period to set the foundation of ROS, Linux, and Python
  knowledge, as well as acquaint students with the RACECAR platform. Everyone started at a slightly 
  different level (some students had prior Python experience, everyone got through different amounts
  of the pre-program coursework), and for the first few days of week one the instructors were 
  primarily concerned with getting all students on a level that would allow them to succeed in the 
  weeks to follow.
  
  In week one groups also were given the task of programming their RACECARs to wall follow -- or, 
  drive forward and stay a specific distance away from a wall -- for ~30 feet as quickly as possible. 
  The cars had to be able to follow both the left and right walls and switch using the buttons on
  the controller. Since all of the cars had the same speed cap (2 meters per second), the only way 
  for teams to differentiate themselves was by having a better algorithm (in terms of computation 
  time and oscillation levels). #EXPLAIN CONTROLLER

  Approach:
  
  To help us with this first challenge, a robotics software engineer from NASA's Jet Propulsion
  Laboratory (JPL), Kyle Edelberg, gave technical lectures on control systems that we could use.

  Process:
  
  My group decided to first implement bang-bang control, and then once we got that working, move on 
  to PID. 

  Results:
  
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
