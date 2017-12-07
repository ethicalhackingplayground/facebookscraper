#
# setup.py
#
# Gets everything ready.
#

# Install setuptools
sudo apt-get install python-setuptools python-dev build-essential

# Install pip
sudo easy_install pip

# Install & upgrade the virtual env
sudo pip install --upgrade virtualenv

# Get geckoddriver from github
sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux32.tar.gz

# Extract the geckodriver file
sudo tar -xvf geckodriver-v0.19.1-linux32.tar.gz

# Remove the old driver from the bin directory
sudo rm /usr/bin/geckodriver

# Copy the new geckodriver to the bin directory
sudo cp geckodriver /usr/bin/

# Remove the geckodriver from the current directory
sudo rm geckodriver

# Remove the geckodriver tar file from the current directory.
sudo rm geckodriver-v0.19.1-linux32.tar.gz

# Create a images directory.
sudo mkdir images


# Install everything that is required.
sudo pip install -r requirements.txt

# Changing home directory permissions
cd $USER && sudo chown -R $USER: $HOME && cd facebookbot
