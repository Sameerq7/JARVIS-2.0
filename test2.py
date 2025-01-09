import os
import tempfile
import webbrowser
import time
import pyautogui
import json
from fuzzywuzzy import process
from myAI import record_audio, save_audio_to_wav, speak_and_play  # Import functions from myAI.py
from google.cloud import speech
import speech_recognition as sr

def transcribe_audio_using_sr(file_path):
    # Using SpeechRecognition library (Google Web Speech)
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Audio could not be understood."
        except sr.RequestError as e:
            return f"Error with the service: {e}"

def transcribe_audio_using_google(file_path):
    # Using Google Cloud Speech-to-Text API
    client = speech.SpeechClient()

    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Returns the first transcription result
    for result in response.results:
        return result.alternatives[0].transcript
    return ""


def load_contacts():
    # Load contacts from the contacts.json file
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        speak_and_play("Contacts file not found.")
        return {}
    except json.JSONDecodeError:
        speak_and_play("Error reading the contacts file.")
        return {}

def match_contact(contact_name, contacts):
    # Use fuzzywuzzy to match the contact name with available contacts
    best_match = process.extractOne(contact_name, contacts.keys())
    if best_match and best_match[1] >= 70:  # 70 is the threshold for matching
        return best_match[0]  # return the contact name with the highest match score
    return None

def whatsapp_messaging():
    contacts = load_contacts()

    if not contacts:
        return

    speak_and_play("Boss, to whom should I message on behalf of you?")
    while True:
        audio = record_audio(duration=5)
        temp_wav_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_wav_filename = temp_wav_file.name
        temp_wav_file.close()
        save_audio_to_wav(audio, 16000, temp_wav_filename)

        # Use SpeechRecognition or Google Cloud Speech-to-Text for transcription
        transcription = transcribe_audio_using_sr(temp_wav_filename)  # Or use transcribe_audio_using_google

        print(f"Transcription: {transcription}")

        contact_name = transcription.capitalize()
        matched_contact = match_contact(contact_name, contacts)

        if matched_contact:
            phone_number = contacts[matched_contact]
            speak_and_play(f"Messaging {matched_contact}.")
            break
        else:
            speak_and_play(f"Contact '{contact_name}' not found. Please try again.")

    speak_and_play(f"Boss, what message do you want to send to {matched_contact}?")
    while True:
        audio = record_audio(duration=5)
        temp_wav_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_wav_filename = temp_wav_file.name
        temp_wav_file.close()
        save_audio_to_wav(audio, 16000, temp_wav_filename)

        # Use SpeechRecognition or Google Cloud Speech-to-Text for transcription
        message = transcribe_audio_using_sr(temp_wav_filename)  # Or use transcribe_audio_using_google

        print(f"Message: {message}")

        speak_and_play(f"Sending message to {matched_contact}: {message}")
        url = f'https://web.whatsapp.com/send?phone={phone_number}&text={message}'
        webbrowser.open(url)

        # Allow time for WhatsApp Web to load and send the message
        time.sleep(10)
        pyautogui.press('enter')
        speak_and_play("Message sent successfully.")
        break

whatsapp_messaging()
