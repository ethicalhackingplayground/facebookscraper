#
# setup.py
#
# Gets everything ready.
#

sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip
sudo pip install --upgrade virtualenv
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux32.tar.gz
tar -xvf geckodriver-v0.19.1-linux32.tar.gz
sudo rm /usr/bin/geckodriver
sudo cp geckodriver /usr/bin/
rm geckodriver
rm geckodriver-v0.19.1-linux32.tar.gz
mkdir images
sudo pip install -r requirements.txt
