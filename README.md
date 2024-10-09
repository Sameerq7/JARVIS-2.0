# JARVIS-2.0
Jarvis is a versatile virtual assistant that performs tasks like code generation, email management, scheduling, weather updates, and news fetching. Integrated with Gemini for real-time information, Jarvis responds to voice commands to manage daily activities seamlessly.

## Description
**Jarvis**: Your Personal Virtual Assistant

**Overview**: Jarvis is an advanced personal virtual assistant designed to simplify daily tasks and enhance productivity through voice commands. It leverages various APIs and built-in functionalities to create a seamless and user-friendly experience.

## Key Features

### Personal Interaction
- Introduces itself and provides personal information upon request.
- Responds to questions about its origin, creator, and relationship with the user.

### Task Management
- Opens and manages applications such as PowerPoint and email clients.
- Sends emails on behalf of the user with simple voice commands.
- Manages and checks the user’s schedule, adding events as needed.

### Information Retrieval
- Accesses Wikipedia to provide summaries and detailed information on various topics.
- Fetches and plays trending news headlines, keeping the user updated.
- Checks weather conditions and retrieves location information.

### File and Document Management
- Reads and scans PDF documents aloud, assisting users in digesting content easily.
- Supports various file operations based on voice commands.

### System Monitoring
- Monitors and reports battery status, internet speed, and system performance.
- Allows the user to shut down, restart, or sleep the system using voice commands.

### Code Generation
- Generates code snippets or entire programs in various programming languages based on the user's problem statement, facilitating rapid development.

### Location Services
- Provides location information and can assist in navigation or retrieving relevant data based on geographical context.

### Social Media Integration
- Opens popular social media platforms like Instagram, WhatsApp, and GitHub seamlessly.
- Checks and reads emails, providing a quick overview of recent messages.

### Voice Recognition and Playback
- Utilizes speech synthesis to provide audio feedback, enhancing user engagement.
- Listens for commands and responds accordingly, making it a hands-free experience.

### Additional Utilities
- Provides real-time updates on various inquiries, from time and date to the weather.
- Can perform calculations, manage files, and execute scripts upon request.

## Technologies Used
- Python for core functionality.
- APIs for news, weather, and Wikipedia access.
- Speech recognition and text-to-speech libraries for interactive user experience.

## Installation Instructions
To get started, create a `.env` file in the root directory of the project and add the following environment variables:

1. **Gemini API Key** (`API_KEY`):
   - To get the Gemini API key, visit the [Gemini API website](https://gemini.com/).
   - Sign up or log in to your account.
   - Navigate to the API section to create a new API key.
   - Copy the generated API key and paste it into your `.env` file.
API_KEY=your_gemini_api_key_here

2. **Email App Password** (`EMAIL_APP_PASSWORD`):
    - If you are using Gmail, you may need to set up [App Passwords](https://support.google.com/accounts/answer/185201) if you have two-factor authentication enabled.
    - Log in to your Google account, go to **Security** settings, and under **Signing in to Google**, look for **App passwords**.
    - Select the app and device you want to generate the password for and click **Generate**.
    - Copy the generated password and paste it into your `.env` file.
EMAIL_APP_PASSWORD=your_email_app_password_here

3. **OpenWeather API Key** (`OPENWEATHER_API_KEY`):
    - Visit the [OpenWeather](https://openweathermap.org/api) website.
    - Sign up for an account if you don’t have one.
    - Once logged in, navigate to the **API keys** section and generate a new API key.
    - Copy the generated API key and paste it into your `.env` file.
OPENWEATHER_API_KEY=your_openweather_api_key_here


4. **News API Key** (`NEWS_API_KEY`):
    - Go to the [News API](https://newsapi.org/) website.
    - Sign up for an account and log in.
    - Navigate to the **API keys** section to obtain your key.
    - Copy the API key and paste it into your `.env` file.
NEWS_API_KEY=your_news_api_key_here


5. **User Email** (`EMAIL`):
    - Enter the email address for which you created the app password in the `.env` file. This email will be used for sending emails.
EMAIL=your_email_id


Install FFmpeg: ffpyplayer relies on FFmpeg for media playback. You may need to install FFmpeg separately. Here’s how:

Windows:

Download the FFmpeg release from [FFmpeg's official website](https://ffmpeg.org/download.html)

Extract the contents to a folder (e.g., C:\ffmpeg).

Add the bin directory to your system PATH:

1. Right-click on **Computer** or **This PC** and select **Properties**.

2. Click on **Advanced system settings** on the left side.

3. Click on **Environment Variables**.

4. Under **System Variables**, scroll down and find the **Path** variable, then click **Edit**

5. Click **New** and enter the path to the bin directory

6. Click **OK** to close all the windows.

**Linux:**

1. **Install FFmpeg**: Download the FFmpeg release from [FFmpeg's official website](https://ffmpeg.org/download.html) and extract it. Then, add the `bin` directory to your system PATH.

2. **Check Python Version Compatibility**: Make sure **ffpyplayer** is compatible with your version of **Python (3.12.2)**. You may want to check the documentation or the **PyPI page for ffpyplayer** for compatibility information.

3. **Run as Administrator**: Sometimes, permission issues can prevent DLLs from loading. Try **running your Python script as an administrator**.

4. **Install Microsoft Visual C++ Redistributable**: If you're on **Windows**, ensure that you have the latest version of the **Microsoft Visual C++ Redistributable** installed. This is often required for many Python libraries that depend on **C/C++ extensions**.

5. **Check for Missing DLLs**: If the error persists, you can use a tool like **Dependency Walker** to check for missing DLLs when trying to load **ffpyplayer**. This tool will help you identify which specific DLLs are causing the issue.


To install the required packages, run:

    "pip install -r requirements.txt"


## Usage Instructions
To run Jarvis, execute the following command in your terminal:

    "python myAI.py"

This will start the Jarvis assistant, and you can interact with it using voice commands or text input.

**Getting Started**

1.After running the application, a GUI will appear.

2.Press ESC to skip the intro or wait for it to complete.

3.Jarvis will give you instructions and prompt you for a password.

4.Enter the password: phenom. (Note: Nothing will appear on the screen while typing. You have 5 attempts to enter the correct password.)

5.If you enter the correct password, Jarvis will greet you with "Welcome back, boss."

**Important Note:**

Make sure to place your actual API keys in the .env file before using Jarvis.

**Custom Prompts**

You can use the following custom prompts to interact with Jarvis:

**1.Introduction:**

"who are you"

"what is your name"

"introduce yourself jarvis"

"introduce yourself"

"tell me something about yourself"

**2.Application Management:**

"open powerpoint"

"open presentation"

"shut down"

"jarvis shutdown the system"

"check battery status"

**3.Email Management:**

"send email"

"jarvis send email to hp@gmail.com"

"jarvis read my emails"

"jarvis check for new messages"

**4.Code Generation:**

"jarvis write code for me"

"generate code for me"

"open code generator"

5.Schedule Management:

"check my schedule"

"what is my schedule today"

"add event"

**6.Weather and Location:**

"check weather"

"open weather"

"location"

**7.News Updates:**

"jarvis give me trending news"

"jarvis what is the news today"

**8.Internet Check:**

"jarvis check internet speed"

"what is my internet speed"

"check internet connection"

**Stopping Jarvis**
To stop Jarvis, you can use the following phrases:

"jarvis stop"

"stop it jarvis"

"shut up jarvis"

"enough jarvis"

"goodbye jarvis"    

## Contact Information
- LinkedIn: [Shaik Sameer Hussain](https://www.linkedin.com/in/shaik-sameer-hussain-b88323250/)
- Email: [9121sameer@gmail.com](mailto:9121sameer@gmail.com)

## Conclusion
Jarvis aims to be the ultimate assistant, simplifying everyday tasks and providing information efficiently. With continuous improvements and feature additions, it strives to adapt to user needs and preferences.
