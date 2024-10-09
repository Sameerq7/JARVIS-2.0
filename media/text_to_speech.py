import pyttsx3
import os
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Directory to save the audio files
output_folder = "C:\\Users\\hp\\Desktop\\JARVIS2.0\\media"
os.makedirs(output_folder, exist_ok=True)

# Get user input for the text command
text_command = input("Enter the text command to convert to audio: ")

# Generate unique output file name
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"startup_message_{timestamp}.wav")

# Generate the audio file
engine.save_to_file(text_command, output_file)
print(f"Created: {output_file}")

# Close the engine
engine.runAndWait()
