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

	# Login to account
	login = browser.find_element_by_id("loginbutton")
	login.send_keys(Keys.ENTER)
	time.sleep(random.uniform(3, 6))
	print "[+] Logged in"

	# Go to the users page.
	if args.hasName == '0':
		goToUserPage("https://www.facebook.com/profile.php?id=" + args.id)
	else:
		if (args.randomsearch == 'male' or args.randomsearch == 'female'):
			randomPage()
		else:
			goToUserPage("https://www.facebook.com/" + args.id)
		

def randomPage ():
	# Search for peoples pages and download there images.
	for i in range(0, args.iterations):
		if (i == args.iterations):
			break
		name=names.get_first_name(gender=args.randomsearch)
		args.id = name
		goToUserPage("https://www.facebook.com/" + args.id)
	print "[+] Successfully download photos"

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
		if args.randomsearch != None:
			print "[+] Trying next person"
			randomPage()
		else:
			print "[!] Try changing the min and max speeds"

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


	#
	# TODO: This needs some work.
	# 
	#for img in soup.find_all("img", class_="_pq3 img"):
		#getimg = str(img.get('style')).strip("background-image: url();")
		#format_1 = string.replace(getimg, '\3a ', ":")
		#format_2 = string.replace(format_1, '\x03d ', "=")
		#format_3 = string.replace(format_2, '\x16 ', "&")
		#format_4 = string.replace(format_3, '\26 ', "&")

		# Append it to the list.
		#images.append(getimg)


	# Check if there are any photos in the array.
	if len(images) > 0:

		if (os.path.exists('images/' + args.id)) == False:
			# Make the directory to store the images
			os.system("mkdir images/" + args.id)

		for image in images:
			print "\n[+] Downloading " + image
			os.system("wget -q " + "'" + image + "'" + " -P images/" + args.id)
	

def Main ():
	
	# Print the banner
	banner()
	
	# Create some arguments.
	parser = argparse.ArgumentParser(description="Downloads images from facebook account")
	required = parser.add_argument_group("Required Arguments")
	optional = parser.add_argument_group("Optional Arguments")
	required.add_argument('-u', '--username', dest='username', help='facebook username', required=True, type=str)
	required.add_argument('-p', '--password', dest='password', help='facebook password', required=True, type=str)
	optional.add_argument('-n', '--hasName' , dest='hasName' , help='Tells us if the account has a name instead of a number', choices=['0','1'], required=False, type=str)
	optional.add_argument('-d', '--id', dest='id', help='facebook id', required=False, type=str)
	optional.add_argument('-r', '--randomsearch', dest='randomsearch', help='randomly goes to someones page and downloads there photos', choices=['male', 'female'], required=False, type=str)
	optional.add_argument('-i', '--iterations', dest='iterations', help='the amount of pages to go through', required=False, type=int)
	global args
	args = parser.parse_args()

	# Login to facebook.
	login(args.username, args.password)
Main()
