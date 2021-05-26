from freedomrobotics.link import Link
    
# Connect to the cloud with Link
# you can instantiate multiple Link objects by using different names (core, my_node1)
freedom = Link("core")
    
# Send your GPS position
freedom.message("/location", \
                "sensor_msgs/NavSatFix", \
                {"latitude": 37.778454,"longitude": -122.389171})
