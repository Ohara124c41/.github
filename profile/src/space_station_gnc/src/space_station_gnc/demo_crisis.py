#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DemoCrisisNode(Node):
    def __init__(self):
        super().__init__('demo_crisis')
        self.get_logger().info('Demo crisis node has started.')
        self.publisher_ = self.create_publisher(String, 'topic', 10)

        # defining time frame: 
        self.Ttimer = 0.1     # ros node loop time
        self.Tsim = 0.01   # simulation time step, ome_max = 1 deg/sec
        self.nsimstep = round(self.Ttimer/self.Tsim)  # nsimstep = Tloop / Tsim 
        self.tcur = 0
        print(self.nsimstep)

        # defining space station
        self.J = (4.15*1000*1000,4.64*1000*1000,19.0*1000*1000) # moment of inertia
        mass = 420000   #420 tons

        # defining errorous engine
        p_err = (-7.0, 7.0, 0.0)
        axis_err = (0.0, 0.0, -1.0)
        F_err = 85.3 * 1000

        # defining CMGs
        ome_cmg = 6600 / 60 * 360 /180 * 3.14159   # 6600rpm 
        p_cmg1 = (3.5, 3.5, 3.0)
        p_cmg2 = (-3.5, 3.5, 3.0)
        p_cmg3 = (-3.5, -3.5, 3.0)
        p_cmg4 = (3.5, -3.5, 3.0)
        axis_cmg1 = (0.0, 0.0, 1.0)
        axis_cmg2 = (0.0, 0.0, 1.0)
        axis_cmg3 = (0.0, 0.0, 1.0)
        axis_cmg4 = (0.0, 0.0, 1.0)


        self.timer = self.create_timer(self.Ttimer, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'tcur= %f' % self.tcur
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.tcur += self.Ttimer

def main(args=None):
    rclpy.init(args=args)
    node = DemoCrisisNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

