import subprocess
import webbrowser
from features.print_slow_and_speak import print_slow_and_speak


applications = {
    "powerpoint": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk",
    "chrome": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk",
    "github": r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\GitHub.lnk",
    "whatsapp": r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\WhatsApp Web.lnk",
    "cmd": r"C:\Windows\System32\cmd.exe"
}


def open_application(app_name):
    print_slow_and_speak(f"OK Boss....Opening {app_name}")
    try:
        if app_name in applications:
            subprocess.Popen([applications[app_name]], shell=True)
        else:
            print_slow_and_speak(f"{app_name} application could not be opened. Please check the name.")
    except Exception as e:
        print_slow_and_speak(f"{app_name} could not be opened. Error: {e}")

def open_url(url, name):
    print_slow_and_speak(f"OK Boss....Opening Your {name}")
    webbrowser.open(url)

def open_github():
    open_url("https://github.com", "GitHub account")

def open_instagram():
    open_url("https://www.instagram.com/h_shaiksameer", "Instagram account")
