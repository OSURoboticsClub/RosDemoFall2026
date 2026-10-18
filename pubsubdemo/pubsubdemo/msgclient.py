import rclpy
from rclpy.node import Node
from rclpy.client import Client

from pubsubdemo_interfaces.srv import StrMsg

# Get string from user
# Send a service request to publish string

class MsgClientNode(Node):
    service: Client

    def loop(self):
        if (self.call_result is None) or (self.call_result is not None) and (self.call_result.done()):
            message = input("Enter a message: ")
        else:
            return
        req = StrMsg.Request()
        req.message = message
        self.call_result = self.service.call_async(req)
        self.call_result.add_done_callback(self.print_result)


    def print_result(self, future):
        print(f"Service has handled {future.result().num} requests.")


    def __init__(self):
        super().__init__("msg_client_node")
        self.service = self.create_client(StrMsg, "/demo/message_service")
        self.create_timer(1.0/10.0, self.loop)
        self.call_result = None


def main(args=None):
    rclpy.init(args=args)

    node = MsgClientNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()