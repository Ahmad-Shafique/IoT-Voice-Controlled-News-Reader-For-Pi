#!/usr/bin/python

import speech_recognition as sr
import pyttsx
import feedparser
from wifi import Cell
from wireless import Wireless
import urllib2
import traceback


def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False


def takeUserVoiceCommandAndReturnText(string):
	r = sr.Recognizer()
	m = sr.Microphone()
	#set threhold level
	with m as source: 
		r.adjust_for_ambient_noise(source)
	print("Set minimum energy threshold to {}".format(r.energy_threshold))
	# obtain audio from the microphone

        try:
            with sr.Microphone() as source:
                print("Say something!")
				readOutTheGivenString(string)
                audio = r.listen(source)
        except Exception,err:
            print Exception,err
	    

	try:
            if internet_on():
                var = r.recognize_google(audio)
                
            else:
                print 'Unable to process online!'
	except Exception,err:
            print Exception,err
	    #print 'found exception'
	    return ''

	print(var)
	return var


def readOutTheGivenString(string):
	try:
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-55)
		engine.say(string);
		engine.runAndWait()
	except Exception,err:
                print Exception,err
                try:
                    raise TypeError("Again ?!?")
                except:
                    pass
                traceback.print_exec()
		#print 'I\'m unable to speak!'
            
		
		
def selectProperUrl(channelName,category):
	if channelName == 'bbc':
		fileName = '/home/pi/Desktop/AutomatedNewsReader/bbc'
	elif channelName == 'cnn':
		fileName = '/home/pi/Desktop/AutomatedNewsReader/cnn'
	with open(fileName) as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 

	category = category.lower()	
	
	for x in content:
		var = x.split(",")
		if category in var[0].lower() :
			return var[1]
	return ''


def readOutTheNewsAsPerUserSelection(channelName, category):
	catLoop = 1	
	
	while catLoop==1:
		url=''
		if channelName == 'bbc' or channelName=='BBC':
			url = selectProperUrl('bbc',category)
		elif channelName=='cnn' or channelName=='CNN':
			url = selectProperUrl('cnn',category)
		elif channelName=='BD News 24' or channelName=='bdnews24' or channelName=='BDNEWS24':
			url = 'http://bdnews24.com/?widgetName=rssfeed&widgetId=1150&getXmlFeed=true'
		
		if url!='':
			break
	
		if url == '' :
			readOutTheGivenString('Category not found under the given channel!')
			readOutTheGivenString('Please speak the category name once again!')
			category = takeUserVoiceCommandAndReturnText()

		if category=='exit' or category=='EXIT':
			readOutTheGivenString('Exiting now...')
			return
	
	d = feedparser.parse(url)
	length = len(d['entries'])

	readOutTheGivenString('If you would like to know the details of any news, please say :\'Describe\'');

	for i in range(0,length):
		readOutTheGivenString(d['entries'][i]['title'])
		
		userInput = takeUserVoiceCommandAndReturnText()
		
		if userInput == 'describe':
			if d['entries'][i]['description'] is None:
				readOutTheGivenString('Sorry, No description available.');
				continue
			else:
				print 'Description:'
				readOutTheGivenString(d['entries'][i]['description'])
				continue
	





def main():
    readOutTheGivenString('Hello sir. I am overwatch. I will be you news reader today.')

    if internet_on() == False :
    	readOutTheGivenString('Sir, I do not detect an internet connection. I need internet to function properly.')
        readOutTheGivenString('I will read out the network names one by one. If you know the  password, press y. Otherwise press n.')
	conn = Cell.all('wlan0')
	for c in conn:
		readOutTheGivenString(c.ssid)
		response = raw_input()
		if response=='n':
			continue
		elif response=='y':
			readOutTheGivenString('Please type in the password')
			p = raw_input('Password : ')
			wireless = Wireless()
			wireless.connect(ssid=c.ssid, password=p)
			break


    readOutTheGivenString('We are online now. Which channel would you like to listen to today ?');
    #userInputChannelName = raw_input()
    userInputChannelName = takeUserVoiceCommandAndReturnText()
    #print va
    count=0
    skipCount = 0;
    if userInputChannelName=='':
	while count==0:
		if skipCount!=0:
			readOutTheGivenString('Sorry sir, I did not recognize the channel. Please speak the channel name once again.');
		skipCount=1
        #readOutTheGivenString('Bainchod ! speak the name properly !!');
		userInputChannelName = takeUserVoiceCommandAndReturnText()
		#userInputChannelName = raw_input()
		if userInputChannelName!='':
                    if userInputChannelName=='BBC' or userInputChannelName=='CNN' or userInputChannelName=='BD NEWS 24':
						break
		if userInputChannelName=='exit' or userInputChannelName=='EXIT':
			sys.exit()

    readOutTheGivenString('You have selected '+userInputChannelName);


    go=0;
    if userInputChannelName=='BD News 24' or userInputChannelName=='bdnews24' or userInputChannelName=='BDNEWS24':
	go = 1;
	readOutTheGivenString('Reading news from {} '.format(userInputChannelName));
	readOutTheNewsAsPerUserSelection(userInputChannelName, '')

    if go==0:
	readOutTheGivenString('Would you like to listen to a specific category? If so, then say the category name. Otherwise say no.');
	userInputCategoryName = takeUserVoiceCommandAndReturnText()
	#userInputCategoryName = raw_input()
	if userInputCategoryName=='':
		while count==0:
			readOutTheGivenString('Sorry sir, I did not understand. Please speak the category name once again.');
                        #readOutTheGivenString('You are a fucking waste of my time. Speak the category again, asshole');
			userInputCategoryName = takeUserVoiceCommandAndReturnText()
			#userInputCategoryName = raw_input()
			if userInputCategoryName!='' or userInputCategoryName=='BBC' or userInputCategoryName=='CNN' or userInputCategoryName=='BD NEWS 24':
				break
	elif userInputCategoryName=='no' or userInputCategoryName=='No' or userInputCategoryName=='NO':
		print 'reading latest news'
		if userInputChannelName.lower()=='bbc':
			userInputCategoryName = 'world'
		elif userInputChannelName.lower()=='cnn':
			userInputCategoryName = 'top'
#	else:
		print 'reading {} news'.format(userInputCategoryName)

	if userInputCategoryName=='no':
            readOutTheGivenString('Reading Latest news from {} '.format(userInputChannelName));
	else:
            readOutTheGivenString('Reading {} news from {} '.format(userInputCategoryName,userInputChannelName));
	readOutTheNewsAsPerUserSelection(userInputChannelName, userInputCategoryName)
	
	
#quit the program

i=0
while i==0:
    main()
	





