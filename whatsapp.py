import pywhatkit as kit
from datetime import datetime, timedelta
import time

# Set the phone number and message
phone_number = "+917993459282"  # Indian number format
message = "Your message from Jarvis"

# Set delays
open_delay = 5  # Seconds to wait before opening WhatsApp
send_delay = 5  # Seconds to wait after opening to send the message

# Calculate current time and target open time
now = datetime.now()
target_open_time = now + timedelta(seconds=open_delay)
open_hour = target_open_time.hour
open_minute = target_open_time.minute

# Adjust if the minute exceeds 59
if open_minute >= 60:
    open_hour += 1
    open_minute = 0

# Check if the scheduled time is within the next minute
if now.hour == open_hour and open_minute <= now.minute + 1:
    open_minute += 1
    if open_minute >= 60:
        open_hour += 1
        open_minute = 0

# Display the scheduled time
print(f"WhatsApp will open at {open_hour:02}:{open_minute:02}.")
time.sleep(open_delay)

# Open WhatsApp Web
kit.sendwhatmsg(phone_number, message, open_hour, open_minute, 0, send_delay)
