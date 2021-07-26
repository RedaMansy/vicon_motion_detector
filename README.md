# vicon_motion_detector
Simple script that subscribes to vicon_bridge and retrieves marker data to determine motion. Create catkin package in src and clone repo into package. 



# Initial Set up

- Connect Vicon PC and Care-o-bot PC to the same network (cob4-13-direct works best)
- Run `connectcob` on Care-o-bot PC to connect to the careobot (make sure the robot is on)
- Run `su robot` to change users and `cd ~/catkin_ws/src` 
- On a Ubuntu 18.04/20.04 machine (henceforth refered to as vicon_bridge PC), git clone the vicon bridge library in your `catkin_ws/src` folder (https://github.com/ethz-asl/vicon_bridge)
- Edit the `datastream_hostport` parameter in the launch file in vicon_bridge package `catkin_ws/src/vicon_bridge/launch/vicon.launch` to have the IP address of the Vicon PC and leave the port number as 801 (making sure it is on the same network as the machine running vicon_bridge).
- On the care-o-bot PC, ensure that the ROS Master is set to the IP address of the PC running the vicon_bridge package, by running `export ROS_MASTER_URI=http://ipaddresshere:11311`. You need to do this on every new terminal you open, I would advise against editing the `~/bashrc` file just in case it messes up any robot configuration, so for now do this step every time.
- Run `roscore` on the vicon_bridge PC and in another terminal run `roslaunch vicon_bridge vicon.launch` making sure that the Vicon PC is running a trial or is in live mode.
- Running `rostopic list` from the care-o-bot PC should now show the published `/vicon/markers` topic, if not it is likely a network issue where you have not set up the ROS master correctly. Refer to this documentation: https://wiki.ros.org/ROS/Tutorials/MultipleMachines and do not forget to **source your workspace and catkin_make.**

# To run motion detection code (after completing above steps)
- On the care-o-bot PC, run `roslaunch cob_bringup robot.launch` in one terminal 
- In another terminal, navigate to you workspace where you have cloned this repo, and run `rosrun marker_package listener.py'
- This may not work depending on how the trial is set up. You will need to figure out which marker to publish by checking the segment_name and marker_name parameters provided by vicon_bridge. An easy way to do so is by running `rosrun marker_package segment_name.py`
