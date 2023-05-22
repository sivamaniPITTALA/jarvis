import speech_recognition as sr
import os
from Jarvis  import MainExe
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=8)  # Set phrase_time_limit for longer phrases, it is Listening Mode...

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
    except:#sr.UnknownValueError
        return "error"

    query = str(query).lower()  # Convert the query to lowercase
    return query 

def WakeupDetected():
    query1 = Listen().lower()

    if "wake up" in query1:
        # os.startfile(r"jarvis_basic\jarvis.py")
        MainExe.Main()
    else:
        pass


while True:
    WakeupDetected()