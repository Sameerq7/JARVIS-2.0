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

def restart_laptop():
    # Prompt the user before restarting the system
    print_slow_and_speak("Boss, have you saved your work? I am going to restart your system. Press 'Enter' to proceed, 'Esc' to cancel, or wait for 5 seconds to restart automatically.")

    # Wait for the user to press 'Enter', 'Esc', or timeout after 5 seconds
    print_slow_and_speak("Waiting for your response...")

    start_time = time.time()
    while time.time() - start_time < 5:  # 5-second window
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':  # 'Enter' key
                print_slow_and_speak("Restarting now, boss.")
                subprocess.run(["shutdown", "/r", "/t", "0"])
                return
            elif key == b'\x1b':  # 'Esc' key
                print_slow_and_speak("Restart cancelled, boss.")
                return

    # If no input within 5 seconds, proceed with restart
    print_slow_and_speak("No response received. Restarting the system now.")
    subprocess.run(["shutdown", "/r", "/t", "0"])

def shutdown_laptop():
    # Prompt the user before shutting down the system
    print_slow_and_speak("Boss, have you saved your work? I am going to shut down your system. Press 'Enter' to proceed, 'Esc' to cancel, or wait for 5 seconds to shut down automatically.")

    # Wait for the user to press 'Enter', 'Esc', or timeout after 5 seconds
    print_slow_and_speak("Waiting for your response...")

    start_time = time.time()
    while time.time() - start_time < 5:  # 5-second window
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':  # 'Enter' key
                print_slow_and_speak("Shutting down now, boss.")
                subprocess.run(["shutdown", "/s", "/t", "0"])
                return
            elif key == b'\x1b':  # 'Esc' key
                print_slow_and_speak("Shutdown cancelled, boss.")
                return

    # If no input within 5 seconds, proceed with shutdown
    print_slow_and_speak("No response received. Shutting down the system now.")
    subprocess.run(["shutdown", "/s", "/t", "0"])