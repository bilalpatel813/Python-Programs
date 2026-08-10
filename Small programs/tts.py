import androidhelper
#import pyttsx3
#from gtts import speak
#engine = pyttsx3.init()
droid =androidhelper.android()
ADMINuser= 'bilal'
ADMINpassword =1234
username=(input('enter your username'))
password =int(input('enter your password'))
if username == ADMINuser and password == ADMINpassword:
    print('logged in')
    droid.ttsSpeak('welcome',ADMINuser)
else:
        print('incorrect password or username')
        droid.ttsSpeak('please enter the correct credentials')
        #engine.runAndWait()
