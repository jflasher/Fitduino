import sys, json
import oauth2 as oauth

sys.path.append('PATH TO FITBIT.py PROJECT')
import fitbit
fb = fitbit.FitBit()

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
#access_token = 'ACCESS_TOKEN'

#6 Make calls with this stored access token
#response = json.loads(fb.ApiCall(access_token, apiCall='/1/user/-/activities/tracker/activeScore/date/today/1d.json'))

#dict = (response['activities-tracker-activeScore'])[0]
#date = dict['dateTime']
#score = dict['value']
#print 'Activity Score of ' + score + ' for ' + date + '.'