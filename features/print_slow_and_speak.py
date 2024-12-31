# import time
# import threading
# from features.speak_and_play import speak_and_play  # Import the speak_and_play function

# def print_slow_and_speak(message, delay=0.1):
#     # Function to print text slowly
#     def print_slow(text, delay):
#         for char in text:
#             print(char, end='', flush=True)  # Print each character with no newline and flush output
#             time.sleep(delay)
#         print()  # Ensure newline after printing

#     # Start the speech playback in a separate thread
#     speech_thread = threading.Thread(target=speak_and_play, args=(message,))
#     speech_thread.start()

#     # Print the message slowly
#     print_slow(message, delay)

#     # Wait for the speech thread to finish
#     speech_thread.join()

# # Usage example
import time
import threading
from features.speak_and_play import speak_and_play  # Import the speak_and_play function

def print_slow_and_speak(message, delay=0.1):
    # Function to print text slowly (printing the entire message at once)
    def print_slow(text, delay):
        #time.sleep(delay)  # Delay before printing the message
        print(text,flush=True)  # Print the entire message normally

    # Start the speech playback in a separate thread
    speech_thread = threading.Thread(target=speak_and_play, args=(message,))
    speech_thread.start()

    # Print the message normally after delay
    print_slow(message, delay)

    # Wait for the speech thread to finish
    speech_thread.join()

# Usage example
