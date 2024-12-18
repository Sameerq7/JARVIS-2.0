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

def get_current_location():
    try:
        ip_add = requests.get('https://api.ipify.org').text
        url = f'https://get.geojs.io/v1/ip/geo/{ip_add}.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        
        city = geo_data.get('city', 'Unknown City')
        state = geo_data.get('region', 'Unknown State')
        country = geo_data.get('country', 'Unknown Country')
        
        location = f"{city}, {state}, {country}"
        
        # Print the current location
        print_slow_and_speak(f"Boss, your current location is: {location}. Checking weather now.")
        
        return city
    
    except Exception as e:
        error_message = f"Error: {e}"
        print_slow_and_speak(error_message)
        return None
    
def get_weather():
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print_slow_and_speak("API key not found.")
        return
    
    # Prompt the user to press Enter or provide city name
    prompt_text = "Press Enter to check the weather, or type the city name to get its weather details."
    # speech_thread = threading.Thread(target=speak_and_play, args=(prompt_text,))
    # speech_thread.start()
    print_slow_and_speak(prompt_text)
    # speech_thread.join()
    
    user_input = input("Enter city name or press Enter to get weather for your current location: ").strip()

    if user_input == "":
        city = get_current_location()
    else:
        city = user_input

    if city:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('cod') != 200:
                error_message = "Request failed."
                print_slow_and_speak(error_message)
                # text_to_speech(error_message, "error.wav")
                # play_audio("error.wav")
                return
            
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            
            # Print the weather information
            weather_report = f"Weather in {city}: {weather.capitalize()}. Temperature: {temp}°C"
            print_slow_and_speak(weather_report)
            
            # Play the weather information as audio
            # text_to_speech(weather_report, "weather_report.wav")
            # play_audio("weather_report.wav")
        
        except requests.RequestException as e:
            error_message = f"Request failed: {e}"
            print_slow_and_speak(error_message)