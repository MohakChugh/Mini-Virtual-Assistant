import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            assistant_speak(ask)
        # assistant_speak("Say Something")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            assistant_speak('I couldnt get that, Sorry')
        except sr.RequestError:
            assistant_speak('Sorry, The internet seems broken or down')
        return voice_data

def assistant_speak(audio_string):
    tts = gTTS(text=audio_string, lang = 'en')
    r = random.randint(1, 100000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print('debug 1')
    playsound.playsound(audio_file)
    print('debug 2')
    print(audio_string)
    print('debug 3')
    os.remove(audio_file)
    print('debug 4')

def respond(voice_data):
    if 'what is your name' in voice_data:
        assistant_speak('My name is Mohak\'s Assistant')
    if 'what time is it' in voice_data:
        assistant_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        assistant_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('where do you want to search for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        assistant_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
assistant_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    assistant_speak(voice_data)
    respond(voice_data)