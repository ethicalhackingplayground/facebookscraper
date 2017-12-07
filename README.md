# facebookscraper

A bot that downloads photos from a facebook page

### Getting Everything Ready
> sudo apt-get update && sudo apt-get upgrade && sudo apt-get install git

### How to download 
> sudo git clone https://github.com/ethicalhackingplayground/facebookscraper.git


### How to Install

> cd facebookscraper && sudo sh setup.sh

### How to get help
> python facebookbot.py -h

usage: facebookbot.py [-h] -u USERNAME -p PASSWORD [-n HASNAME] [-d ID]
                      [-r RANDOMSEARCH] [-i ITERATIONS]
                
                   
### Arguments

- -u the username of your facebook account (required)

- -p the password of your facebook account (required)

- -n if the account has a name use this argument 
looks like "http://www.facebook.com/name_here"

- -d if the account has a facebook id use this argument   
looks like "https://www.facebook.com/profile.php?id=id_here"

- -r argument randomly searches through pages on facebook and downloads there images

- -i is the amount of pages to search for


### Examples

- python facebookbot.py -u username -p password -d xxxxxxxxx 
- python facebookbot.py -u username -p password -r male -i 20
- python facebookbot.py -u username -p password -r female -i 20


Happy hacking. ;)


