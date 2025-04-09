import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry,Path
from geometry_msgs.msg import PoseStamped


class SimpleTrajectory(Node):
    def __init__(self):
        super().__init__("simple_trajectory")


        self.odom_sub_ = self.create_subscription(Odometry,"bumperbot_controller/odom", self.odomCallback, 10)
        self.trajectory_pub_ = self.create_publisher(Path, "/bumperbot_controller/trajectory", 10)

        self.trajectory_ = Path()
        self.trajectory_.header.frame_id = "odom"

        self.get_logger().info("Trajectory Node started!! Looking for Odometry Messages")
        

        

  
    def odomCallback(self, msg):

        pose_stamped  = PoseStamped()
        pose_stamped.header = msg.header
        pose_stamped.pose = msg.pose.pose

        self.trajectory_.poses.append(pose_stamped)
        self.trajectory_.header.stamp = self.get_clock().now().to_msg()

        self.trajectory_pub_.publish(self.trajectory_)
        self.get_logger().info("Publishing Path ....")


        

def main():
    rclpy.init()
    simple_tra = SimpleTrajectory()
    rclpy.spin(simple_tra)
    simple_tra.destroy_node()
    rclpy.shutdown()




if __name__=="__main__":
    main()
