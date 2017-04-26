#!/usr/bin/python

import speech_recognition as sr
import pyttsx
import feedparser

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
		
		
def selectProperUrl(channelName,category):
	if channelName == 'bbc':
		
	elif channelName == 'cnn':
		


def readOutTheNewsAsPerUserSelection(channelName, category):
	if channelName == 'bbc' or channelName=='BBC': 
		url = selectProperUrl('bbc',category)
	elif channelName=='cnn' or channelName=='CNN':
		url = selectProperUrl('cnn',category)
	elif channelName=='BD News 24' or channelName=='bdnews24' or channelName=='BDNEWS24':
		url = 'http://bdnews24.com/?widgetName=rssfeed&widgetId=1150&getXmlFeed=true'
		
	d = feedparser.parse(url)
	length = len(d['entries'])

	readOutTheGivenString('If you would like to know the details of any news, please say :\'Describe\'');

	for i in range(0,length):
		readOutTheGivenString(d['entries'][i]['title'])
		
		userInput = takeUserVoiceCommandAndReturnText()
		
		if userInput == 'describe'
			if d['entries'][i]['description'] is None:
				readOutTheGivenString('Sorry, No description available.');
				continue
			else:
				print 'Description:'
				readOutTheGivenString(d['entries'][i]['description'])
	




readOutTheGivenString('Hello sir. Which channel would you like to listen to today ?');
userInputChannelName = takeUserVoiceCommandAndReturnText()
#print va
if userInputChannelName=='':
	count=0
	while count==0:
		readOutTheGivenString('Sorry sir, I did not understand. Please speak the channel name once again.');
		userInputChannelName = takeUserVoiceCommandAndReturnText()
		if userInputChannelName!='':
			break

readOutTheGivenString('You have selected '+userInputChannelName);


go=0;
if channelName=='BD News 24' or channelName=='bdnews24' or channelName=='BDNEWS24':
	go = 1;
	readOutTheGivenString('Reading news from {} '.format(userInputChannelName));
	readOutTheNewsAsPerUserSelection(userInputChannelName, '')

if go==0:
	readOutTheGivenString('Would you like to listen to a specific category? If so, then say the category name. Otherwise say no.');
	userInputCategoryName = takeUserVoiceCommandAndReturnText()
	if userInputCategoryName=='':
		while count==0:
			readOutTheGivenString('Sorry sir, I did not understand. Please speak the channel name once again.');
			userInputCategoryName = takeUserVoiceCommandAndReturnText()
			if userInputCategoryName!='':
				break
	elif userInputCategoryName=='no' or userInputCategoryName=='No' or userInputCategoryName=='NO':
		print 'reading latest news'
		userInputCategoryName = 'latest'
	else:
		print 'reading {} news'.format(userInputCategoryName)
	
	readOutTheGivenString('Reading {} news from {} '.format(userInputCategoryName,userInputChannelName));
	readOutTheNewsAsPerUserSelection(userInputChannelName, userInputCategoryName)
	
	
#quit the program
	
	





