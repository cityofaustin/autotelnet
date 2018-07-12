from flask import Flask, render_template, request
from IPINFO import *
import telnetlib

app = Flask(__name__)

def clean_ip(ip):
	return None

@app.route('/')
def my_form():
	return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():

	ip = request.form["ip"]

	if ip in IPINFO:
		clean_ip(ip)

	else:
		return ("Invalid IP address, please refresh the page and enter again")

@app.route('/confirmation')
def confirmation():
	ip = my_form_post
	return('contents on {ip} is about to be cleaned')

if __name__ == "__main__":
	app.run(debug = True)



	# print(processed_text)

