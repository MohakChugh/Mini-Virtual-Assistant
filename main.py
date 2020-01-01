import speech_recognition as sr
import webbrowser
import time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print("Say Something")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('I couldnt get that, Sorry')
        except sr.RequestError:
            print('Sorry, The internet seems broken or down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Mohak\'s Assistant')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('where do you want to search for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
print('How can I help you?')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)