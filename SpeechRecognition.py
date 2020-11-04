from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
from time import ctime
import time
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import playsound
from gtts import gTTS

# root window

root = tk.ThemedTk()
root.get_themes()
root.set_theme('scidgreen')
root.resizable(0, 0)
root.configure(background='white')
root.title('Voice Assistant')


def speak(audio_string):
    # Convert String to Voice
    tts = gTTS(text=audio_string, lang='en')
    # Output file
    tts.save('hello.mp3')
    # Plays audio_file
    playsound.playsound("./hello.mp3")
    # remove the file after stop
    os.remove('hello.mp3')


def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)

        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Did not get that")
        except sr.RequestError:
            speak("Network Problem , Try again")

        return voice_data


def respond(voice_data):
    if 'name' in voice_data:
        speak("My name is Iman")
    if 'time' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = record_audio("what are you locking for?")
        url = 'https://google.com/search?q=' + str(search)
        webbrowser.get().open(url)
    if 'find location' in voice_data:
        location = record_audio('Which location you want to search for ?')
        url = 'https://google.nl/maps/place' + str(location)
        webbrowser.get().open(url)
        speak('Here is your location ' + str(location) + '/&amp;')
    if 'exit' in voice_data:
        speak("bye")
        root.destroy()


def task():
    speak('Hi ! I am Iman, your new assistant . How can I help you ?')
    voice_data = record_audio()
    respond(voice_data)


task_btn = ttk.Button(root, text='Start', width=10, command=task).grid(row=0, column=0, ipady=20, ipadx=90)
save_btn = ttk.Button(root, text='Exit', width=10, command=root.destroy).grid(row=1, column=0, ipady=20, ipadx=90)
root.mainloop()

