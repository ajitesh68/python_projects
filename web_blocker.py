import time 
from datetime import datetime as dt

ip_locatime = "127.0.0.1"
website_list=["www.facebook.com","www.instagram.com"]

host_path="/etc/hosts"
startime="09.0.0"
endtime="18.0.0"

now=dt.now()
current_time=now.strftime("%H:%H:%S")
print(current_time)
while True:
    if startime<=current_time and current_time<=endtime:
        print("working hours")
        with open(host_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(ip_locatime+" "+website+"\n")
    else:
        print("Non working hour")
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

                file.truncate()                    
    time.sleep(10)