
import os, configparser
from configparser import ConfigParser

dir_name= os.path.dirname(os.path.abspath(__file__))
configur=ConfigParser()
configur.read('{}/requirement.ini'.format(dir_name))
def check_ping(hostname):
    res=os.system("ping -c 4 "+ hostname)
    if res==0:
        print("Ping Successfull")
    else:
        ("ping Failed")  

if __name__=="__main__":
    hostname=configur.get("Section1","hostname")
    check_ping(hostname)
    print(hostname)          