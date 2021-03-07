# Autonomous Vehicles Capstone: Odometry and IMU 

We are Team 4 in the Autonomous Vehicles Data Science Capstone Project. Our project revolves around the IMU, Odometry efforts while we collectively work to build a 1/5 scale racing autonomous vehicle. The goal for our project was to calibrate, tune, and analyze Odometry and IMU data to obtain the most accurate position estimate, compass heading, and data readings to support the other subteams that would utilize these measurements in the navigation stack.

For this project we will be using the F110th Odometry files to gather odometry data using our robot car and integrating, calibrating, and verifying the OpenLog Artemis IMU for our project.

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
