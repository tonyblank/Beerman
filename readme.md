## Install

# Set up fresh raspberry pi
* grab raspian image and set up sd card
*     https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi
* boot up pi
* configure wlan usb card
*     http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/

# install dependencies
* sudo apt-get update
* sudo apt-get install python-dev
* sudo apt-get install python-rpi.gpio
* follow steps here: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c (even though unsure if we'll use i2c, get it working regardless)
* install easy_install and pip to get python packages
*     sudo apt-get install python-setuptools
*     sudo easy_install pip
* install python dependencies
*     sudo pip install simplejson
*     sudo pip install httplib2
*     sudo pip install python-oauth2
*     sudo pip install twitter


# shopping list
* longer wire for flow sensors
* something to perm. attach sensor to wires (coupler?)
* more 8gig sd cards
* tubing for flow sensors (includes clamps on each end)