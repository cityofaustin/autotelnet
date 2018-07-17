#Get and set libraries
import getpass
import sys
import telnetlib
import time

#Chooses test controller IP address for testing
HOST = "172.16.122.76"


#password = getpass.getpass()


#sets up telnet
tn=telnetlib.Telnet(HOST, timeout=5)
#Default password for D4 telnets
pass1="austin"
time.sleep(2)

#sends login info to controller
tn.write((pass1+"\r\n").encode('ascii'))
time.sleep(2)
tn.write((pass1+"\r\n").encode('ascii'))
time.sleep(2)

#Sets up page access
command1="0"
command2="1"
#Goes to status options
tn.write(command1.encode('ascii'))
time.sleep(2)
#Goes to main status page
tn.write(command2.encode('ascii'))
#Ends telnet session
tn.close()
