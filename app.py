from flask import Flask, render_template, request
import speech_recognition as sr
import os
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)
    text =  recognizer.recognize_google(audio, language = "ES")
    if(text.lower() =="abrir chrome"):
        resH = subprocess.Popen("start chrome", shell=True, stdout=subprocess.PIPE)
        outH = resH.stdout.read()
    print("Has dicho: " + text)
    return render_template('index.html', text = text)