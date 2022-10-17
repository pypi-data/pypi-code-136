try:
    import rclpy

    from .ros2_numpy.point_cloud2 import *
except:
    try:
        import rospy

        from .ros_numpy.point_cloud2 import *
        from .ddynamic_reconfigure_python.ddynamic_reconfigure import \
            DDynamicReconfigure
    except:
        raise ImportError("Please install ROS2 or ROS1")
