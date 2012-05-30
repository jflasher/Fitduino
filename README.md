Fitduino
========

Intended to be a project using the Arduino platform to provide a physical representation of your Fitbit statistics.

## Requirements
FitBit.py project - https://github.com/jflasher/FitBit.py
python-oauth2 project - https://github.com/dgouldin/python-oauth2
pySerial - http://pyserial.sourceforge.net/

## Usage
Directions are inline in fitduino.py. It's a couple of copy/paste steps to work through the oauth process. Honestly, it's a bit confusing but a one time thing to set up for something hacky. Obviously, if this is intended for wider distribution, something else needs to be done.

Currently, the fitduino.py program will contact the Fitbit servers and request activity data. Based on that data, it will calculate 1 of 3 bins that you're activity is currently in and send out a message over the serial port. The formula is as follows:

	(3 * minutesVeryActive + 2 * minutesFairlyActive  + minutesLightlyActive) / minutesSedentary
	
The fitduino Arduino sketch is set up to monitor the serial port (hardcoded into fitduino.py) for a single number, either 0, 1 or 2 to indicate activity level. When it receives something in the serial buffer, the sketch will flash all the lights and then show a happy face (2), a normal face (1) or a sad face (0). 

If you set up the fitduino.py to run on a cron job or some other repeatable timer, the system will become a visual indication of your overall activity level during the day.

This is just meant as a simple way to see your Fitbit data in a different way. If you have any questions, let me know!