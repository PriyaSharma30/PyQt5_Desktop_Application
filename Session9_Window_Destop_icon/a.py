import os 
# configparser
# from configparser import ConfigParser

# dir_name= os.path.dirname(os.path.abspath(__file__))
# configur=ConfigParser()
# configur.read('{}/requirement.ini'.format(dir_name))
def check_ping(hostname):
    res=os.system("ping  "+ hostname)
    if res==0:
        print("Ping Successfull")
    else:
        ("ping Failed")  

if __name__=="__main__":
    hostname="172.17.207.232"
    check_ping(hostname)
    print(hostname)       