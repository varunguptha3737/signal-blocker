import gpsd
import time
import os

# Connect to the GPSD daemon
gpsd.connect()

# Continuously get the GPS data
while True:
    # Get the GPS data
    gps_data = gpsd.get_current()
    
    # Check if GPS data is valid
    if gps_data.mode >= 2:
        # Get the latitude and longitude
        lat = gps_data.lat
        lon = gps_data.lon
        
        # Use the latitude and longitude to determine the location
        location = "Latitude: " + str(lat) + " Longitude: " + str(lon)
        print("Location: " + location)
        
        # Use the os module to run a shell command to detect cell phone signals
        os.system("rtl_power -f 400M:480M:1M -g 50 -i 1m -e 1h power.csv")
        
        # Parse the output of the shell command to identify the frequencies of nearby cell phone signals
        with open("power.csv") as f:
            lines = f.readlines()
            for line in lines:
                if "Cell" in line:
                    # Extract the frequency of the cell phone signal
                    frequency = line.split(",")[0]
                    print("Cell phone signal detected at frequency: " + frequency)
                    
        # Wait before getting the next GPS data
        time.sleep(5)
