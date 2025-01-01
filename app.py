from flask import Flask, render_template, request, Response
import subprocess
import os
import random
import time

app = Flask(__name__)
process = None  # Global variable to manage the subprocess

# List of random statements for the frontend
statements = [
    "Welcome to Jarvis, your personal assistant.",
    "Jarvis is powered by artificial intelligence.",
    "Created with ❤️ by Sameer, an aspiring developer.",
    "Jarvis learns and evolves with time.",
    "Your requests are my command!",
    "Jarvis will assist you in managing your tasks effortlessly.",
    "Jarvis is ready to serve you!",
    "Every task is an opportunity for Jarvis to shine.",
    "Jarvis, your personal assistant, always at your service.",
    "You are just a command away from Jarvis's help.",
    "With Jarvis, your productivity reaches new heights.",
    "Feel free to ask Jarvis anything. I'm always here.",
    "Jarvis will handle it for you.",
    "Your personal AI assistant, powered by Jarvis.",
    "Jarvis is more than just a voice—it's a revolution.",
    "Everything is possible with Jarvis on your side.",
    "Jarvis: A blend of intelligence and innovation.",
    "Jarvis adapts to your needs with every interaction.",
    "Your digital companion is ready to assist—just ask.",
    "Jarvis is the future of personal assistance.",
    "With Jarvis, managing tasks has never been easier."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_jarvis():
    global process
    if not process:
        process = subprocess.Popen(
            [".venv/Scripts/python.exe", "-u", "myAI.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
    return {"status": "Jarvis started"}

@app.route("/stop", methods=["POST"])
def stop_jarvis():
    global process
    if process:
        process.terminate()
        process = None
    return {"status": "Jarvis stopped"}

@app.route("/logs")
def stream_logs():
    global process
    if not process:
        return "No process running", 400

    def generate():
        while True:
            output = process.stdout.readline()
            if output:  # Stream output immediately
                yield f"data: {output.strip()}\n\n"
            elif process.poll() is not None:  # Exit if the process ends
                break

    return Response(generate(), mimetype="text/event-stream")

@app.route("/random-statement")
def random_statement():
    # Randomly select a statement from the list
    statement = random.choice(statements)
    return {"statement": statement}

if __name__ == "__main__":
    app.run(debug=True)
