#!/usr/bin/python
#
# Title: facebookbot.py
# Author: Th3j0K3r
#
# Description: Downloads images from a facebook account.
#
import names
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import string

def banner():
	os.system('clear')
	print """
 _______  _______  _______  _______  _______  _______  _______  ___   _    _______  _______  _______ 
|       ||   _   ||       ||       ||  _    ||       ||       ||   | | |  |  _    ||       ||       |
|    ___||  |_|  ||       ||    ___|| |_|   ||   _   ||   _   ||   |_| |  | |_|   ||   _   ||_     _|
|   |___ |       ||       ||   |___ |       ||  | |  ||  | |  ||      _|  |       ||  | |  |  |   |  
|    ___||       ||      _||    ___||  _   | |  |_|  ||  |_|  ||     |_   |  _   | |  |_|  |  |   |  
|   |    |   _   ||     |_ |   |___ | |_|   ||       ||       ||    _  |  | |_|   ||       |  |   |  
|___|    |__| |__||_______||_______||_______||_______||_______||___| |_|  |_______||_______|  |___|  

				<<Facebook Image Scraper>>
\n\n"""
	

def login (username, password):

	# Create the driver.
	global browser
	browser = webdriver.Firefox()
	browser.get("http://www.facebook.com")

	# Find some login elements.
	userID = browser.find_element_by_id("email")
	passID = browser.find_element_by_id("pass")

	# Send the username & password to the browser
	userID.send_keys(username)
	passID.send_keys(password)

	time.sleep(3)
	if 'https://www.facebook.com/login.php?login_attempt' in browser.current_url:
		print "[!] Wrong password"
		return

	# Login to account
	login = browser.find_element_by_id("loginbutton")
	login.send_keys(Keys.ENTER)
	time.sleep(random.uniform(3, 6))
	print "[+] Logged in"

	# Go to the users page.
	if args.hasName == '0':
		goToUserPage("https://www.facebook.com/profile.php?id=" + args.id)
	else:
		randomPage()
		if args.id != None:
			goToUserPage("https://www.facebook.com/" + args.id)
		

def randomPage ():
	for i in range(0, args.iterations):
		name=names.get_first_name(gender=args.randompage)
		args.id = name
		goToUserPage("https://www.facebook.com/" + args.id)

def goToUserPage (url):
	
	print "[+] Navigating to account " + url	

	# Go to the users page
 	browser.get(url)
	time.sleep(random.uniform(3, 6))

	try:

		# Go to the pages to download the images.
		GoToPage("Photos")
		GoToPage("Albums")
		GoToPage("Featured Photos")
	except:
		# Start the random download again.
		if args.randompage != None:
			print "[+] Trying next person"
			randomPage()

def GoToPage (link):
	
	# Go to there images page.
	print "[+] Navigating to the " + link
	browser.find_element_by_link_text(link).click()
	time.sleep(random.uniform(3, 6))
	getImages(browser.current_url)
	
	

def getImages (currentUrl):
	
	print "\n[+] Fetching Images from " + currentUrl 
	response = browser.page_source
	soup = BeautifulSoup(response, 'html.parser')

	images = []
	for img in soup.find_all("i", class_="uiMediaThumbImg"):
		getimg = str(img.get('style')).strip("background-image: url();")
		# Append it to the list.
		images.append(getimg)	


	for img in soup.find_all("img", class_="_pq3 img"):
		getimg = str(img.get('style')).strip("background-image: url();")
		#format_1 = string.replace(getimg, '\3a ', ":")
		#format_2 = string.replace(format_1, '\x03d ', "=")
		#format_3 = string.replace(format_2, '\x16 ', "&")
		#format_4 = string.replace(format_3, '\26 ', "&")

		# Append it to the list.
		images.append(getimg)


	# Check if there are any photos in the array.
	if len(images) > 0:

		if (os.path.exists('images/' + args.id)) == False:
			# Make the directory to store the images
			os.system("sudo mkdir images/" + args.id)

		for image in images:
			print "\n[+] Downloading " + image
			os.system("wget -q " + "'" + image + "'" + " -P images/" + args.id)

	# Start the random download again.
	if args.randompage != None:
		randomPage()
	

def Main ():
	
	# Print the banner
	banner()
	
	# Create some arguments.
	parser = argparse.ArgumentParser(description="Downloads images from facebook account")
	parser.add_argument('-u', '--username', dest='username', help='facebook username', required=True, type=str)
	parser.add_argument('-p', '--password', dest='password', help='facebook password', required=True, type=str)
	parser.add_argument('-n', '--hasName' , dest='hasName' , help='Tells us if the account has a name instead of a number - 1 for yes and 0 for no', required=False, type=str)
	parser.add_argument('-i', '--id', dest='id', help='facebook id', required=False, type=int)
	parser.add_argument('-r', '--random', dest='randompage', help='randomly goes to someones page and downloads there photos - male / female', required=False, type=str)
	parser.add_argument('-s', '--iterations', dest='iterations', help='the amount of pages to go through', required=False, type=int)

	global args
	args = parser.parse_args()

	# Login to facebook.
	login(args.username, args.password)


Main()
