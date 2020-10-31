from tkinter import *
import task as task
from ttkthemes import themed_tk as tk
from tkinter import ttk
from time import ctime
import time
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import playsound
import random
from gtts import gTTS


def speak(audio_string):
    # Convert String to Voice
    tts = gTTS(text=audio_string, lang='en')
    # Produce random numbers from 1 to 10000000
    r = random.randint(1, 10000000)
    # Output file
    audio_file = 'audio-' + str(r) + '.mp3'
