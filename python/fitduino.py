import sys, json
import oauth2 as oauth
import serial

sys.path.append('PATH TO FITBIT.py PROJECT')
import fitbit
fb = fitbit.FitBit()

# Try to get the serial port
try:
	ser = serial.Serial('/dev/tty.usbmodemfa141', 9600)
except serial.serialutil.SerialException:
	sys.exit()

################
## Variables
highScore = 0.5 # 60/120/120
mediumScore = 0.2 # 0/60/120
################

#1. Get the auth_url and auth_token
#auth_url, auth_token = z.GetRequestToken()
#print 'auth_url: '  + auth_url

#2. Go to the auth_url and Allow
#3. Save out the auth_token so it can be stored below
#print 'auth_token: ' + auth_token.to_string()
#s = 'AUTH_TOKEN'
#auth_token = oauth.Token.from_string(s)

#4 THIS WILL ONLY WORK ONCE - generate a access_token with the PIN and auth_token
#access_token = z.GetAccessToken(PIN, auth_token)

#5 Get this access_token and save it to a string below
access_token = 'ACCESS_TOKEN'

#6 Make calls with this stored access token
# We want to get a whole bunch of activity stats

# Minutes
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/minutesSedentary/date/today/1d.json'))
minutesSedentary = float(response['activities-minutesSedentary'][0]['value'])
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/minutesLightlyActive/date/today/1d.json'))
minutesLightlyActive = float(response['activities-minutesLightlyActive'][0]['value'])
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/minutesFairlyActive/date/today/1d.json'))
minutesFairlyActive = float(response['activities-minutesFairlyActive'][0]['value'])
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/minutesVeryActive/date/today/1d.json'))
minutesVeryActive = float(response['activities-minutesVeryActive'][0]['value'])

# Active score
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/activeScore/date/today/1d.json'))
activeScore = float(response['activities-activeScore'][0]['value'])

# Activity calories
response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/activityCalories/date/today/1d.json'))
activityCalories = float(response['activities-activityCalories'][0]['value'])

print str(minutesSedentary) + ', ' + str(minutesLightlyActive) + ', ' + str(minutesFairlyActive) + ', ' + str(minutesVeryActive) + ', ' + str(activeScore) + ', ' + str(activityCalories)

# We will have 3 levels, 0, 1 and 2. 0 Being lowest and 2 being highest activity value
# fake values for now
minutesVeryActive = 100
minutesFairlyActive = 120
minutesLightlyActive = 120
minutesSedentary = 1440 - minutesVeryActive - minutesFairlyActive - minutesLightlyActive
score = (3. * minutesVeryActive + 2. * minutesFairlyActive + minutesLightlyActive) / minutesSedentary
print score

# See what level we fall into
scoreLevel = 0
if score >= highScore:
	scoreLevel = 2
elif score >= mediumScore:
	scoreLevel = 1
print scoreLevel

# Send the score to the serial port
string = str(scoreLevel)
ser.write(string)