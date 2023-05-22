import speech_recognition as sr
import os
import subprocess
import pyttsx3
import sqlite3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize the database connection
conn = sqlite3.connect('jarvis.db')
c = conn.cursor()

# Create a table to store user input and AI responses
c.execute('''CREATE TABLE IF NOT EXISTS conversations
             (id INTEGER PRIMARY KEY AUTOINCREMENT, input TEXT, response TEXT)''')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Use microphone as input source
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

if __name__ == "__main__":
    # Use Google Speech Recognition to transcribe the audio
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        
        # Check for specific keywords in the user's input
        if "hi jarvis" in text.lower():
            speak("Hello, how can I assist you?")
            
        elif "open" in text:
            app = text.split("open ")[-1]
            os.system("open -a " + app) # Use the "open" command to launch the app on a Mac
            # For Windows, use "os.startfile(app)"
        
        elif "shut down" in text:
            os.system("shutdown /s /t 1") # Use the "shutdown" command to shut down the computer on Windows
            # For Mac, use "sudo shutdown -h now"
        
        elif "reset" in text:
            subprocess.call(["sudo", "reboot"]) # Use the "reboot" command to restart the computer
        else:
            speak("I'm sorry, I didn't understand that.")
            print("Sorry, I didn't understand that.")
        
        # Store the conversation in the database
        c.execute("INSERT INTO conversations (input, response) VALUES (?, ?)", (text, "response"))
        conn.commit()

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        print("Sorry, I didn't catch that. Could you please repeat?")

    except sr.RequestError as e:
        speak("Sorry, my speech service is down. Please try again later.")
        print("Could not request results from speech recognition service; {0}".format(e))
