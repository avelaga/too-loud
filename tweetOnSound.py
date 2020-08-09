import RPi.GPIO as GPIO
import random
from twython import Twython
from keys import apiKey, apiSecret, accessToken, accessTokenSecret

#https://twitter.com/testpibot
tweetStr = "abhi is a butt"
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

GPIO.setmode(GPIO.BCM)
sensorPin = 18
GPIO.setup(sensorPin, GPIO.IN)

tweetTimeout = 0
timeoutMax = 5000000 # # of cycles before tweeting is enabled again

complaints = [
	"IT'S SO LOUD IN HERE",
	"GOD DAMN WHY ARE YOU HUMANS SO LOUD",
	"SHUT. UP.",
	"OH MY GOD I CAN'T HEAR MYSELF COMPUTING",
	"please quiet down...",
	"LET ME SIT IN PEACE"
]

while True:
	# sensor heard loud sound
	if GPIO.input(sensorPin) == 0:
		# but only tweet if it's been awhile. it would spam tweets otherwise
		if tweetTimeout == 0:
			randomIndex = random.randint(0, len(complaints) - 1)
			tweetStr = complaints[randomIndex]
			print(tweetStr)
			#api.update_status(status=tweetStr)
			tweetTimeout = timeoutMax
	if tweetTimeout > 0:
		tweetTimeout -= 1
