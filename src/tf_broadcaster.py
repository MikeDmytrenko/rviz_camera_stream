#!/usr/bin/env python3  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


def handle_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "map"
    t.child_frame_id = "camera1"
    t.transform.translation.x = msg.linear.x
    t.transform.translation.y = msg.linear.y
    t.transform.translation.z = -50.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    # turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/body_pose',
                     geometry_msgs.msg.Twist,
                     handle_pose,
                     )
    rospy.spin()