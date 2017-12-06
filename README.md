# facebookscraper

A bot that downloads photos from a facebook page

### Getting it ready

> sh setup.sh

### How to get help
> python facebookbot.py -h

usage: facebookbot.py [-h] -u USERNAME -p PASSWORD [-n HASNAME] [-i ID]
                      [-r RANDOMPAGE] [-s ITERATIONS]
                      

> -u the username of your facebook account (required)
> -p the password of your facebook account (required)
> -n if the account has a name instead use this argument  
looks like "http://www.facebook.com/name_here"

> -i if the account has a facebook id use this argument   
looks like "https://www.facebook.com/profile.php?id=id_here"

> -r argument randomly searches through pages on facebook and downloads there images
> -s is the amount of pages to search for


### Examples

- python facebookbot.py -u username -p password -i xxxxxxxxx 
- python facebookbot.py -u username -p password -r male -s 20
- python facebookbot.py -u username -p password -r female -s 20


Happy hacking. ;)


