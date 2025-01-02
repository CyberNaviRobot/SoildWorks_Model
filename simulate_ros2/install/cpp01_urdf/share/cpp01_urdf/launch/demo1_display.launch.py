from launch import LaunchDescription
from launch_ros.actions import Node

# 封装终端指令相关类
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# 文件包含相关
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# 分组相关
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# 事件相关
# from launch.event_handlers import OnProcessStart,OnProcessExit
# from launch.actions import ExecuteProcess,RegisterEventHandler,LogInfo
# 获取功能包下share目录或路径
from ament_index_python.packages import get_package_share_directory

from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command

import os

cpp01_urdf_dir = get_package_share_directory("cpp01_urdf")

default_model_path = os.path.join(cpp01_urdf_dir,"urdf/urdf","CyberNaviRobot.urdf")
default_rviz_path = os.path.join(cpp01_urdf_dir,"rviz","urdf.rviz")

model = DeclareLaunchArgument(name="model",default_value=default_model_path)

p_value = ParameterValue(Command(["xacro ",LaunchConfiguration("model")]))
robot_state_pub = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    parameters=[{"robot_description":p_value}]
)

# 关节信息节点(建议)
# joint_state_pub = Node(
#     package="joint_state_publisher",
#     executable="joint_state_publisher"
# )

# 关节信息节点图形界面
joint_state_pub = Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui"
)

rviz2 = Node(
    package="rviz2",
    executable="rviz2",
#    arguments=["-d",get_package_share_directory("cpp06_urdf") + "/rviz/urdf.rviz"]
    arguments=["-d",default_rviz_path]

    )

def generate_launch_description():
    return LaunchDescription([model,robot_state_pub,joint_state_pub,rviz2])