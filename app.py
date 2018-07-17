from flask import Flask, render_template, request
from IPINFO import *
import getpass
import sys
import telnetlib
import time

def reset(HOST):


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


app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():

	ip = request.form["ip"]

	if ip in IPINFO:
		reset(ip)

	else:
		return ("Invalid IP address, please refresh the page and try again")

@app.route('/confirmation')
def confirmation():
	return('contents on {ip} is about to be cleaned')

if __name__ == "__main__":
	app.run(debug = True)



	# print(processed_text)

