import rclpy
from rclpy.node import Node

from pubsubdemo_interfaces.srv import StrMsg
from std_msgs.msg import String


class MsgServiceNode(Node):
    """ 
    Service Server
    Recieve a string request
        - Publishes requested string to /demo/topic
        - Responds with the number of messages recieved
    """
    def handle_msg(self, request: StrMsg.Request, response: StrMsg.Response) -> StrMsg.Response:

        #publish messsage string
        message = String()
        message.data = request.message
        self.publisher.publish(message)

        #increment request count
        self.requests_received += 1

        #respond with request count
        response.num = self.requests_received
        return response


    def __init__(self):
        super().__init__("msg_service")
        self.publisher = self.create_publisher(String, "/demo/topic", 10)
        self.service   = self.create_service(StrMsg, "/demo/message_service", self.handle_msg)
        self.requests_received = 0


def main(args=None):
    rclpy.init(args=args)

    node = MsgServiceNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()