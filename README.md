# 🤖 Differential-Drive-Bot ROS 2 Project

This project implements a mobile differential drive robot using ROS 2, featuring motor control, odometry computation, and sensor fusion using a Kalman Filter. It is designed to work in a simulation or real-world environment and is compatible with visualization tools like PlotJuggler.

---

## 📦 Features

- ✅ **Wheel-based velocity control** (converts `/cmd_vel` to wheel velocities)
- ✅ **Odometry calculation** using wheel encoders
- ✅ **TF broadcasting** (`odom → base_footprint`)
- ✅ **Sensor fusion** with IMU using a **Kalman Filter**
- ✅ **Data visualization** using PlotJuggler

---

## 🗂️ Packages

### 🔹 `bumperbot_description`
- Contains the robot's URDF, Gazebo, and ROS 2 Control configuration files.
- Launches RViz and Gazebo simulation.
- Files:
  - `bumperbot.urdf.xacro`
  - `bumperbot_gazebo.xacro`
  - `bumperbot_ros2_control.xacro`
  - Launch: `display.launch.py`, `gazebo.launch.py`

### 🔹 `bumperbot_controller`
  - Contains the robot's Yaml for setting parameters for bumperbot_controller,Nodes for controlling robot.
  - Launches controller.
  - Converts high-level velocity commands into wheel speeds and publishes them to the robot’s velocity controller.
  - Computes and publishes real-time odometry and TF based on wheel encoder feedback for localization and path tracking.
  - Files:
  - `simple_controller.py`
  - `noisy_controller.py`
  - `bumperbot_controller.yaml`
  - Launch: `controller.launch.py`, `keyboard_teleop.launch.py`
### 🔹 `bumperbot_utilis`
  - Contains the trajctory node.
  - Continuously builds a trajectory path by subscribing to odometry data.
  - Publishes the robot's path as a nav_msgs/Path message for real-time visualization in RViz.
  - Files:
  - `trajectory.py`
### 🔹 `bumperbot_localization`
  - Contains the kalman filter node, imu republisher node.
  - Launches a static transform between base_footprint_ekf and imu_link_ekf, which is needed to align the IMU frame with the robot base for sensor fusion.
  - Starts the ekf_node from robot_localization, loading configuration from ekf.yaml to perform sensor fusion (e.g., IMU + odometry).
  - Launches imu_republisher.py, a custom node that  reformats or filters IMU messages to match the expected format for the EKF.
  - Files:
  - `kalman_filter.py`
  - `imu_republisher.py`
  - `local_localization.launch.py`

    

  
    
    










