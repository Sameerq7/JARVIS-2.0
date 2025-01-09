import requests
import os
import threading
import speech_recognition as sr
from dotenv import load_dotenv
from features.speak_and_play import speak_and_play

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_news(query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'sortBy': 'relevancy',
        'pageSize': 5  # Limit to top 5 articles
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def fetch_and_play_news():
    speak_and_play("Please tell me the news topic you are interested in.")
    
    # Initialize recognizer for speech input
    recognizer = sr.Recognizer()
    attempts = 0
    query = ""

    # Use the microphone as source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while attempts < 3:
            try:
                print("Listening for news topic...")
                audio = recognizer.listen(source, timeout=5)
                query = recognizer.recognize_google(audio)
                print(f"User said: {query}")
                
                # Check if user said "stop", "nothing", or "return"
                if query.lower() in ["stop", "nothing", "return"]:
                    speak_and_play("Stopping the news fetch operation.")
                    return  # Exit the function if user says stop/nothing/return
                
                speak_and_play(f"Fetching news on {query}...")
                break  # Break the loop if recognition is successful
            except sr.UnknownValueError:
                attempts += 1
                speak_and_play("Sorry, I couldn't understand the audio. Please try again.")
                if attempts == 3:
                    speak_and_play("I couldn't understand the topic after multiple attempts. Please try again later.")
                    return
            except sr.RequestError as e:
                speak_and_play(f"Could not request results from Google Speech Recognition service; {e}")
                return

    stop_playing = False  # Flag to control news playback

    def play_news(news_data):
        nonlocal stop_playing
        articles = news_data.get('articles', [])
        if articles:
            for article in articles:
                if stop_playing:
                    break  # Exit if playback is stopped
                title = article['title']
                description = article['description']
                
                # Print the news article before playing it
                print(f"Title: {title}")
                print(f"Description: {description}\n")
                
                speak_and_play(f"Title: {title}. Description: {description}.")
        else:
            speak_and_play("No articles found for the specified query.")

    def stop_news_playback():
        nonlocal stop_playing
        stop_playing = True  # Set the flag to stop playback

    news_data = get_news(query)
    if news_data:
        # Start news playback in a new thread
        threading.Thread(target=play_news, args=(news_data,)).start()

        print("Press Enter to stop playback...")
        input()  # Wait for user input to stop playback
        stop_news_playback()
    else:
        speak_and_play("Failed to retrieve news.")


