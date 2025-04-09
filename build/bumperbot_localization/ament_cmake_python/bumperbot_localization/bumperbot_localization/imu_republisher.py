#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
import time
from sensor_msgs.msg import Imu

imu_publisher = None


def imuCallback(imu):
    global imu_publisher
    imu.header.frame_id = "base_footprint_ekf"
    imu_publisher.publish(imu)




def main():
    global imu_publisher
    rclpy.init()
    node = Node("imu_republisher_node")

    imu_publisher = node.create_publisher(Imu, "imu_ekf", 10)
    imu_subcriber = node.create_subscription(Imu, "imu/out", imuCallback, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
