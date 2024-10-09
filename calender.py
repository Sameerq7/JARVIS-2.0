import os
import pickle
import tempfile
import pyttsx3
import keyboard
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta
import pygame
from pydub import AudioSegment

SCOPES = ['https://www.googleapis.com/auth/calendar']

pygame.init()
pygame.mixer.init()
def text_to_speech(text, filename):
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        temp_filename = temp_file.name
    engine.save_to_file(text, temp_filename)
    engine.runAndWait()
    audio = AudioSegment.from_wav(temp_filename)
    audio.export(filename, format="wav")
    os.remove(temp_filename)

def speak_and_play(prompt):
    unique_filename = f"C:/Users/hp/Desktop/JARVIS2.0/temp/{datetime.now().strftime('%Y%m%d_%H%M%S')}_summary.wav"
    text_to_speech(prompt, unique_filename)
    play_audio(unique_filename)

def play_audio(file_path):
    if os.path.isfile(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Audio file not found: {file_path}")

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:/Users/hp/Desktop/JARVIS2.0/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def get_events():
    service = authenticate_google_calendar()
    now = datetime.now(timezone.utc).isoformat()
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        NoUpcoming = "Boss....! There is no schedule fixed for you."
        print('No upcoming events found.')
        speak_and_play(NoUpcoming)
        return

    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)

    for event in events:
        print("Press 'Enter' to view the next event or 'Esc' to exit.")
        speak_and_play("Boss..! Please Press 'Enter' to view the next event or 'Esc' to exit")
        # Wait for user input
        while True:
            if keyboard.is_pressed('enter'):
                break
            elif keyboard.is_pressed('esc'):
                print("Stopping event retrieval.")
                speak_and_play("Stopping event retrieval, Boss!")
                return
        
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        description = event.get('description', 'Boss....! You did not specify anything for this event.')

        # Convert the start date-time to a date object
        start_dt = datetime.fromisoformat(start[:-6])  # Removes the timezone part
        event_date = start_dt.date()
        formatted_time = start_dt.strftime("%I:%M %p")

        # Check if the event is today or tomorrow
        if event_date == today:
            date_text = "today"
        elif event_date == tomorrow:
            date_text = "tomorrow"
        else:
            date_text = start_dt.strftime("%d %B %Y")

        # Print and speak event details
        print(summary)
        print(description)
        message = f"Boss....! You have scheduled '{summary}' at {formatted_time} {date_text}. {description}"
        speak_and_play(message)




def add_event():
    service = authenticate_google_calendar()
    
    speak_and_play("Boss..! Please Enter title of the event")
    title = input("Boss..! Please Enter title of the event: ")
    speak_and_play("Now Enter event description")
    description = input("Now Enter event description: ")
    speak_and_play("Enter year")
    year = int(input("Enter year (YYYY): "))
    speak_and_play("Enter month")
    month = int(input("Enter month (MM): "))
    speak_and_play("Enter day")
    day = int(input("Enter day (DD): "))
    speak_and_play("Enter time....! or press Enter for default timing")
    time = input("Enter time (HH:MM:SS, or press Enter for default 12:00:00): ") or "12:00:00"
    
    month_str = f"{month:02d}"
    day_str = f"{day:02d}"
    
    start_time = f"{year}-{month_str}-{day_str}T{time}+05:30"
    end_time = f"{year}-{month_str}-{day_str}T{time}+05:30"
    
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
    }
    
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
        success_message = "BOSS....! SCHEDULED FIXED FOR YOU SUCCESSFULLY"
        speak_and_play(success_message)
    except Exception as e:
        print(f"An error occurred: {e}")


def update_event():
    service = authenticate_google_calendar()
    
    upcoming_events = service.events().list(calendarId='primary', maxResults=5, singleEvents=True,
                                            orderBy='startTime').execute()
    events = upcoming_events.get('items', [])
    
    if not events:
        message = "No upcoming events found."
        print(message)
        speak_and_play(message)
        return

    for event in events:
        event_id = event['id']
        event_summary = event['summary']
        event_start = event['start'].get('dateTime', event['start'].get('date'))
        event_description = event.get('description', 'No description')
        print(f"Event ID: {event_id}")
        print(f"Summary: {event_summary}")
        print(f"Start: {event_start}")
        print(f"Description: {event_description}\n")  # New line for better readability

        speak_and_play(f"Event title: {event_summary}. Description: {event_description}")
    speak_and_play("Boss...! Please Enter the title of the event to update")
    event_title = input("Boss...! Please Enter the title of the event to update: ")
    speak_and_play("Enter new description for the event")
    updated_description = input("Enter new description for the event: ")

    for event in events:
        if event['summary'] == event_title:
            event_id = event['id']
            event = service.events().get(calendarId='primary', eventId=event_id).execute()
            event['description'] = updated_description
            updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
            message = f"Event updated: {updated_event.get('summary')}"
            print(message)
            speak_and_play(updated_event.get('summary'))  # Play only the updated event title
            return

    message = "No event found with that title."
    print(message)
    speak_and_play(message)

def delete_event_by_title():
    service = authenticate_google_calendar()
    event_title = input("Enter the title of the event to delete: ")
    now = datetime.now(timezone.utc).isoformat()
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True).execute()
    events = events_result.get('items', [])
    
    for event in events:
        if event.get('summary') == event_title:
            event_id = event['id']
            service.events().delete(calendarId='primary', eventId=event_id).execute()
            print(f"Deleted event: {event_id}")
            return  # Delete one event and exit after confirmation

    print("No event found with the specified title.")

def menu():
    while True:
        print("\nGoogle Calendar Menu:")
        print("1. Display upcoming events")
        print("2. Add an event")
        print("3. Update an event")
        print("4. Delete an event")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            get_events()

        elif choice == '2':
            add_event()

        elif choice == '3':
            update_event()

        elif choice == '4':
            delete_event_by_title()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
