import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
#set threhold level
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
# obtain audio from the microphone

go=0
while go==0:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        var = r.recognize_google(audio)
        print(var)
    except Exception,err:
        print Exception,err
