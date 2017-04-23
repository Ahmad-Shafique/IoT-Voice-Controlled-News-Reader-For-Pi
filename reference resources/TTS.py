import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-55)
engine.say('Hello , whats your name ?');
engine.say('I am mr. robot. What news would you like to listen to today ?');
#engine.say('Sally sells seashells by the seashore.')
#engine.say('Sally sells seashells by the seashore.')

#voices = engine.getProperty('voices')
#for voice in voices:
#   engine.setProperty('voice', voice.id)
#   engine.say('The quick brown fox jumped over the lazy dog.')

#engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
