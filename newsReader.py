#!/usr/bin/python

import speech_recognition as sr
import pyttsx

def takeUserVoiceCommandAndReturnText():
	r = sr.Recognizer()
	m = sr.Microphone()
	#set threhold level
	with m as source: 
		r.adjust_for_ambient_noise(source)
	#print("Set minimum energy threshold to {}".format(r.energy_threshold))
	# obtain audio from the microphone

	with sr.Microphone() as source:
		#print("Say something!")
		audio = r.listen(source)

	try:
		var = r.recognize_google(audio)
	except:
		#print 'found exception'
		return ''

#	print(var)
	return var


def readOutTheGivenString(string):
	try:
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-55)
		engine.say(string);
		engine.runAndWait()
	except:
		print 'I\'m unable to speak!'



readOutTheGivenString('Hello sir. Which channel would you like to listen to today ?');
userInputChannelName = takeUserVoiceCommandAndReturnText()
#print va
if userInputChannelName=='':
	readOutTheGivenString('Sorry sir, I did not understand. Please speak the channel name once again.');
else :
	readOutTheGivenString('You have selected '+userInputChannelName);
	readOutTheGivenString('Would you like to listen to a specific category? If so, then say the category name. Otherwise say no.');
	userInputCategoryName = takeUserVoiceCommandAndReturnText()
	if userInputCategoryName=='':
		readOutTheGivenString('Sorry sir, I did not understand. Please speak the category name once again.');
	elif userInputCategoryName=='no' or userInputCategoryName=='No' or userInputCategoryName=='NO':
		print 'reading latest news'
	else:
		print 'reading {} news'.format(userInputCategoryName)
	
	





