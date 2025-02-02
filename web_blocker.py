import time 
from datetime import datetime as dt  # Import datetime module to handle time

# IP address used for redirecting blocked websites (localhost)
ip_locatime = "127.0.0.1"

# List of websites to be blocked
website_list = ["www.facebook.com", "www.instagram.com"]

# Path to the system's hosts file (used for blocking websites)
host_path = "/etc/hosts"

# Define working hours (blocking time) using datetime objects
startime = dt.strptime("09:00:00", "%H:%M:%S").time()  # Start blocking at 9:00 AM
endtime = dt.strptime("21:00:00", "%H:%M:%S").time()    # Stop blocking at 9:00 PM

# Infinite loop to continuously check the time and block/unblock websites
while True:
    now = dt.now().time()  # Get current system time dynamically
    print(f"Current time: {now}")  # Print current time for debugging

    # If current time is within the blocking hours
    if startime <= now <= endtime:
        print("Working hours: Blocking websites")

        # Open the hosts file in read & write mode ('r+')
        with open(host_path, "r+") as file:
            content = file.read()  # Read the entire file content

            # Check if websites are already blocked, if not, block them
            for website in website_list:
                if website not in content:  # If website entry is not in the file
                    file.write(ip_locatime + " " + website + "\n")  # Add to hosts file
    else:
        print("Non-working hours: Unblocking websites")

        # Open the hosts file in read & write mode
        with open(host_path, "r+") as file:
            content = file.readlines()  # Read all lines into a list
            file.seek(0)  # Move cursor to the beginning of the file

            # Write back only lines that do not contain blocked websites
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()  # Truncate the file to remove extra data

    time.sleep(10)  # Wait for 10 seconds before checking again
