cmake_minimum_required(VERSION 2.8.3)
project(ros_pickle)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

# catkin_python_setup()

# Generate messages in the 'msg' folder
add_message_files(
  FILES
  Pickle.msg
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros_pickle
#  CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

