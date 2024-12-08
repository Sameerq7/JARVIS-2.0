import wave
import numpy as np
import pyttsx3
import os
import re
import msvcrt 
import getpass
from google.api_core.exceptions import InternalServerError
from threading import Thread
import smtplib
import simpleaudio as sa
from threading import Thread, Event
from features.checkInternet import *
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import keyboard
from features.news import fetch_and_play_news
from tkinter import messagebox, font
import geocoder
import tkinter as tk
import requests
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import psutil
from PyPDF2 import PdfReader
import pygame
from ffpyplayer.player import MediaPlayer
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime, timezone,timedelta
import subprocess
from features.copyMatter_from_Wikipedia import create_gui
from pydub import AudioSegment
import webbrowser
import sys
import cv2
import time
import warnings
import tempfile
import whisper
import sounddevice as sd
from features.prints import print_slow
from features.print_slow_and_speak import print_slow_and_speak
from features.reademail import read_recent_emails
from features.playalong import *

def PlayVideo2(video_path):
    def extract_audio(video_path, audio_path):
        command = [
            'ffmpeg', '-i', video_path, 
            '-q:a', '0', '-map', 'a', audio_path
        ]
        with open(os.devnull, 'w') as devnull:
            subprocess.run(command, stdout=devnull, stderr=devnull)

    def play_audio(filename, stop_event):
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        
        while not stop_event.is_set() and play_obj.is_playing():
            pass

    audio_path = "audio.wav"  # Temporary audio file
    extract_audio(video_path, audio_path)  # Extract audio from video

    stop_event = Event()  # Create an event to stop audio playback
    
    # Load the video
    video = cv2.VideoCapture(video_path)

    # Set the window to full screen
    cv2.namedWindow("Starting JARVIS 2.0", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Starting JARVIS 2.0", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Start audio in a separate thread
    audio_thread = Thread(target=play_audio, args=(audio_path, stop_event))
    audio_thread.start()
    
    while True:
        grabbed, frame = video.read()

        if not grabbed:
            print_slow_and_speak("System Started Boss")
            break

        # Display the video frame
        cv2.imshow("Starting JARVIS 2.0", frame)

        # Check for 'Esc' key press
        key = cv2.waitKey(28)  # Adjust as needed
        if key == 27:  # 27 is the ASCII code for the Esc key
            stop_event.set()  # Signal the audio thread to stop
            break

    video.release()
    cv2.destroyAllWindows()
    audio_thread.join()  # Wait for the audio thread to finish

    # Clean up the temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)

def PlayVideo(video_path):
    def PlayAudio(get_frame, player):
        while True:
            frame, val = get_frame()
            if val != 'eof' and frame is not None:
                img, t = frame
            else:
                break

    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    
    # Set the window to full screen
    cv2.namedWindow("StartIng JARVIS 2.0", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("StartIng JARVIS 2.0", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()

        if not grabbed:
            print_slow_and_speak("System Started Boss")
            break

        # Show the video frame
        cv2.imshow("StartIng JARVIS 2.0", frame)

        # Check for 'Esc' key press
        key = cv2.waitKey(28)
        if key == 27:  # 27 is the ASCII code for the Esc key
            break
        
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame

    video.release()
    cv2.destroyAllWindows()