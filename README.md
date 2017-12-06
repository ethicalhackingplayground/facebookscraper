# facebookscraper

A bot that downloads photos from a facebook page

### Getting it ready

> sh setup.sh

### How to get help
> python facebookbot.py -h

usage: facebookbot.py [-h] -u USERNAME -p PASSWORD [-n HASNAME] [-i ID]
                      [-r RANDOMPAGE] [-s ITERATIONS]

Downloads images from facebook account

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        facebook username
  -p PASSWORD, --password PASSWORD
                        facebook password
  -n HASNAME, --hasName HASNAME
                        Tells us if the account has a name instead of a number
                        - 1 for yes and 0 for no
  -i ID, --id ID        facebook id
  -r RANDOMPAGE, --random RANDOMPAGE
                        randomly goes to someones page and downloads there
                        photos - male / female
  -s ITERATIONS, --iterations ITERATIONS
                        the amount of pages to go through

**** -u the username of your facebook account (required)
**** -p the password of your facebook account (required)
**** -n if the account has a name instead use this argument  
looks like "http://www.facebook.com/name_here"

**** -i if the account has a facebook id use this argument 
looks like "https://www.facebook.com/profile.php?id=id_here"

**** -r argument randomly searches through pages on facebook and downloads there images
**** -s is the amount of pages to search for


### Examples

- python facebookbot.py -u username -p password -i xxxxxxxxx 
- python facebookbot.py -u username -p password -r male -s 20
- python facebookbot.py -u username -p password -r female -s 20


