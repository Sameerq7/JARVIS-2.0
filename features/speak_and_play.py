import pyttsx3
import tempfile
import os
import pygame
from pydub import AudioSegment
from datetime import datetime

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=8192)

def text_to_speech(text, filename):
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        temp_filename = temp_file.name
    engine.save_to_file(text, temp_filename)
    engine.runAndWait()
    audio = AudioSegment.from_wav(temp_filename)
    audio.export(filename, format="wav")
    os.remove(temp_filename)

def play_audio(file_path):
    if os.path.isfile(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Audio file not found: {file_path}")

def speak_and_play(prompt):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    temp_dir = os.path.join(base_dir, "temp")  # Create a temp directory path relative to the script
    os.makedirs(temp_dir, exist_ok=True)  # Ensure the temp directory exists
    unique_filename = os.path.join(temp_dir, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_summary.wav")  # Construct the full file path
    text_to_speech(prompt, unique_filename)
    play_audio(unique_filename)
