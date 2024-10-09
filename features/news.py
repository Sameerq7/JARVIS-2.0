import requests
import os
import threading
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
    speak_and_play("Enter news topic")
    query = input("Enter news topic: ")  # Ask for user input directly
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

