import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher

from std_msgs.msg import String


class PublisherNode(Node):
    publisher: Publisher

    def publish_msg(self):
        msg = String()
        msg.data = "Hello World!"
        self.publisher.publish(msg)
        self.get_logger().info("Published Message")

    def __init__(self):
        super().__init__("demo_publisher_node")
        self.publisher = self.create_publisher(String, "/demo/topic", 10)
        self.create_timer(2.0, self.publish_msg)


def main(args=None):
    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()