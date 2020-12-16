#! /usr/bin/env python

import rospy
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
import math

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('node_controller', anonymous=True)
robot=moveit_commander.RobotCommander()

arm_group=moveit_commander.MoveGroupCommander("ur5_1_planning_group")
hand_group=moveit_commander.MoveGroupCommander("gripper")




#open gripper
hand_group.set_named_target("open")
plan2=hand_group.go()

# OBJECT 1
#arm 1st grabbing position

list_joint_angles=[math.radians(-9.35256127763),
                   math.radians(-70.6116506803), 
                   math.radians(100.702779077), 
                   math.radians(239.745121795),
                   math.radians(269.890243393), 
                   math.radians(-44.2766386957)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)

# arm 2nd grabbing position
list_joint_angles=[math.radians(-11.2247457199),
                   math.radians(320.697963999), 
                   math.radians(71.3120990942), 
                   math.radians(57.8247629324),
                   math.radians(90.110400878), 
                   math.radians(136.968851495)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)

#close hand
hand_group.set_named_target("close")
plan2=hand_group.go()

arm_group.set_named_target("obj1")
plan1=arm_group.go()

# arm 3rd grabbing position
list_joint_angles=[math.radians(-85.816423075),
                   math.radians(-127.264141767), 
                   math.radians(-53.2525051666), 
                   math.radians(-89.6187649198),
                   math.radians(-270.128397619), 
                   math.radians(59.2559608903)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)

#open gripper
hand_group.set_named_target("open")
plan2=hand_group.go()

# object 2
#arm 1st grabbing position

list_joint_angles=[math.radians(14.3842240152),
                   math.radians(-68.1135561839), 
                   math.radians(118.950382616), 
                   math.radians(219.051218065),
                   math.radians(269.840263153), 
                   math.radians(-31.4591399195)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)

# arm 2nd grabbing position
list_joint_angles=[math.radians(14.3709650605),
                   math.radians(-64.0026599797), 
                   math.radians(119.909790374), 
                   math.radians(213.979937007),
                   math.radians(269.832702479), 
                   math.radians(-31.4766339738)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)
# arm 2nd grabbing position
list_joint_angles=[math.radians(-11.2247457199),
                   math.radians(320.697963999), 
                   math.radians(71.3120990942), 
                   math.radians(57.8247629324),
                   math.radians(90.110400878), 
                   math.radians(136.968851495)]

joint_goal = arm_group.set_joint_value_target(list_joint_angles)
arm_group.go(joint_goal, wait=True)
#close hand
hand_group.set_named_target("close")
plan2=hand_group.go()

# arm 2nd grabbing position
list_joint_angles=[math.radians(-94.0267179873),
                   math.radians(-54.1188754157), 
                   math.radians(33.9385131506), 
                   math.radians(290.0434588),
                   math.radians(270.142519934), 
                   math.radians(-51.8727962251)]

#open gripper
hand_group.set_named_target("open")
plan2=hand_group.go()

rospy.sleep(5)
moveit_commander.roscpp_shutdown()

