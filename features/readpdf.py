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


def read_pdf_and_play_audio():
    # Replace audio prompts with print_slow_and_speak
    print_slow_and_speak("Boss...Can you Please provide the path to the PDF file.")
    
    # Ask the user to enter the file path of the PDF
    pdf_path = input("Please enter the path to the PDF file: ").strip()
    
    # Remove double quotes from the path
    sanitized_pdf_path = pdf_path.replace('"', '')

    # Check if the sanitized PDF file path exists
    if not os.path.isfile(sanitized_pdf_path):
        # Inform the user that the path does not exist
        print_slow_and_speak("The specified PDF file does not exist. Please check the path and try again.")
        return

    # Read the PDF content
    def read_pdf_with_pypdf2(file_path):
        pdf_content = ""
        try:
            with open(file_path, "rb") as file:
                reader = PdfReader(file)
                for page in reader.pages:
                    pdf_content += page.extract_text() + "\n"
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
        return pdf_content

    pdf_content = read_pdf_with_pypdf2(sanitized_pdf_path)
    
    if pdf_content:
        # Inform the user that the content is being printed
        print_slow_and_speak("Printing the PDF content.")
        print("PDF Content:")
        print(pdf_content)
    else:
        # Inform the user that no content was found
        print_slow_and_speak("No content found in the PDF.")