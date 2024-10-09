import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from features.speak_and_play import speak_and_play
import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    speak_and_play("Checking internet speed. Please wait.")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    speed_report = (f"Boss...Your download speed is {download_speed:.2f} Mbps, "
                    f"upload speed is {upload_speed:.2f} Mbps, "
                    f"and your ping is {ping} ms.")
    print(speed_report)
    speak_and_play(speed_report)

