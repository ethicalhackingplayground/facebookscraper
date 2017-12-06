#
# setup.py
#
# Gets everything ready.
#

sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip
sudo pip install --upgrade virtualenv
mkdir images
sudo pip install -r requirements.txt
