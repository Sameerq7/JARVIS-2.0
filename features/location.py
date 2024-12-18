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

def get_location_info():
    prompt_message = "Boss.....! Please Enter the destination: "
    
    # Convert the prompt to speech and play it
    print_slow_and_speak(prompt_message)
    
    # Wait for the prompt to finish before asking for input
    destination = input(prompt_message)
    
    def loc(place):
        try:
            geolocator = Nominatim(user_agent="myUniqueAppName")
            location = geolocator.geocode(place, addressdetails=True)
            
            if not location:
                return None, {'error': 'Location not found'}, None
            
            target_latlng = (location.latitude, location.longitude)
            target_location = location.raw['address']
            target_info = {
                'city': target_location.get('city', 'Unknown City'),
                'state': target_location.get('state', 'Unknown State'),
                'country': target_location.get('country', 'Unknown Country')
            }

            current_loc = geocoder.ip('me')
            current_latlng = current_loc.latlng
            
            if not current_latlng:
                return None, {'error': 'Current location not found'}, None
            
            distance = str(great_circle(current_latlng, target_latlng))
            distance = str(distance.split(' ', 1)[0])
            distance = round(float(distance), 2)

            return current_latlng, target_info, distance
        except Exception as e:
            print(f"Error during geocoding: {e}")
            return None, {'error': str(e)}, None

    def my_location():
        try:
            ip_add = requests.get('https://api.ipify.org').text
            url = f'https://get.geojs.io/v1/ip/geo/{ip_add}.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            
            city = geo_data.get('city', 'Unknown City')
            state = geo_data.get('region', 'Unknown State')
            country = geo_data.get('country', 'Unknown Country')
            postal = geo_data.get('postal', 'Unknown Postal Code')
            
            return city, state, country, postal
        except Exception as e:
            print(f"Error getting IP location: {e}")
            return "Unknown City", "Unknown State", "Unknown Country", "Unknown Postal Code"

    current_latlng, destination_info, distance = loc(destination)
    
    if current_latlng and destination_info:
        current_city, current_state, current_country, postal_code = my_location()
        
        # Form the message with a newline between current location and destination
        message = (f"Current Location: {current_city}, {current_state}, {current_country}.\n"
                   f"Destination: {destination_info['city']}, {destination_info['state']}, {destination_info['country']}.\n"
                   f"Boss, The Distance to destination is: {distance} km.")
        
        print_slow_and_speak(message)
        
    else:
        error_message = destination_info['error']
        print_slow_and_speak(error_message)