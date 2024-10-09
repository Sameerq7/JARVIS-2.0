import time
import sys
import threading
from features.speak_and_play import speak_and_play  # Import the speak_and_play function

def print_slow_and_speak(message, delay=0.1):
    # Function to print text slowly
    def print_slow(text, delay):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')  # Ensure newline after printing

    # Start the speech playback in a separate thread
    speech_thread = threading.Thread(target=speak_and_play, args=(message,))
    speech_thread.start()

    # Print the message slowly
    print_slow(message, delay)

    # Wait for the speech thread to finish
    speech_thread.join()

# Usage example

