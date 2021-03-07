# Autonomous Vehicles Capstone: Odometry and IMU 


We are Team 4 in the Autonomous Vehicles Data Science Capstone Project. Our project revolves around the IMU, Odometry efforts while we collectively work to build a 1/5 scale racing autonomous vehicle. The goal for our project was to calibrate, tune, and analyze Odometry and IMU data to obtain the most accurate position estimate, compass heading, and data readings to support the other subteams that would utilize these measurements in the navigation stack.

For this project we will be using the F110th Odometry files to gather odometry data using our robot car and integrating, calibrating, and verifying the OpenLog Artemis IMU for our project.

For a vehicle to successfully navigate istelf and even race autonomously, it is essential for the vehicle to be able localize itself within its environment. This is where Odometry and IMU data can greatly support the robot’s navigational ability. Wheel Odometry provides useful measurements to estimate the position of the car through the use of wheel’s circumference and rotations per second. IMU, which stands for Interial Measurement Unit, is 9 axis sensor that can sense linear acceleration, angular velocity, and magnetic fields. Together, these data sources can provide us crucial information in deriving a Position Estimate (how far our robot has traveled) and a Compass Heading (orientation of the robot/where it’s headed).

While most navigation stacks rely on GPS or Computer Vision to achieve successful navigation, this leaves the robot vulnerable to unfavorable scenarios. For example, GPS is prone to lag and may be infeasible in unfamiliar terrain. Computer Vision approaches often depend heavily on training data and cannot always provide continouos and accurate orientation. Odometry and IMU readings are thus invaluable sources of sensing information that can easily complement and enhance navigational stacks in place to build more robust and accurate autonomous navigation models.

Our problem investigates using IMU and Odometry sensors to aid in this mission by providing relevant data, position estimates, and vehicle heading in cases when GPS and other mapping are not reliable, or to supplement these approaches. IMU (Inertial  Measurement  Unit) provides linear acceleration, angular velocity, and magnetic force sensing ability through the use of accelorometers, gyroscopes, and occasionally magnetometers.  Wheel Odometry  also provide  useful  measurements  to  estimate the  position  of  the  car  through  the use of the wheel’s circumference and rotations per second. Together, these  sensors provide relevant and invaluable data that can be fused to obtain a primary heading and position estimate for the robot. Furthermore, these sensors can be fused with navigation and obstacle avoidance systems already in place to build more robust and accurate autonomous navigation models.

Our aim is to calibrate, tune, and analyze Odometry and IMU data to provide most accurate Position Estimate, Heading, and data readings to achieve high performant autonomous navigation and racing ability.

Developed by: Pranav Deshmane and Sally Poon

### Usage

```
python run.py <target>
```
The Targets are: 
 
* `conversion` - This will extract the data from the raw ROS bags, clean them, and convert them to csv files to be analyzed
 
* `viz_analysis` - This will run the visualizations used in our analysis for IMU and Odometry calibration, tuning, and testing

* `test` - This will test the conversion and visualization process with sample data chosen from our raw data

### Resources

### Additional ROS package 
`ros_imu_yaw_pkg` is an ROS package we developed to aid in the integration of the OLA Artemis IMU to ROS. It allows the orientation quaternion readings derived from the IMU to be easily converted into Euler angles and Yaw heading. This is to improve the debugging process within ROS and helps to easily visualize the Yaw heading. This package can be run in parallel as a complement to the main ROS package used to interface with the OLA Artemis IMU and can easily integrate with the rest of your current ROS system in place as a separate node. Overall, this is to aid in the development process within ROS when deriving Yaw Heading from the OLA Artemis IMU. 


## IMU

### OpenLog Artemis IMU

### Calibration

### Heading/Visualization

## Analysis

## Odometry

### Tuning

### Position Estimate
