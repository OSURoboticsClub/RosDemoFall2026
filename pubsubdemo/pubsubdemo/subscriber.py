import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):

    def on_recv(self, msg: String):
        self.get_logger().info(msg.data)


    def __init__(self):
        super().__init__("demo_subscriber_node")
        self.create_subscription(String, "/demo/topic", self.on_recv, 10)



def main(args=None):
    
    rclpy.init(args=args)

    node = SubscriberNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()