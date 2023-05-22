import openai 
import speech_recognition as sr
import os
import subprocess
import pyttsx3
import sqlite3
import requests
import json 
import time 
import webbrowser
import bs4

# Set your OpenAI API key 
openai.api_key = "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"

# Initialize the text-to-speech engine. 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Define function to transcribe audio to text
def transcribe_audio_to_text(filename): 
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source: 
        audio = recognizer.record(source) 
    try: 
        return recognizer.recognize_google(audio) 
    except: 
        print('Skipping unknown error') 
        speak('Skipping unknown error') 

# Define function to generate AI response using OpenAI's GPT-3
def generate_response(prompt): 
    try:
        response = openai.Completion.create( 
            engine="text-davinci-003",
            prompt=prompt, 
            max_tokens=4000, 
            n=1, 
            stop=None, 
            temperature=0.5, 
        ) 
        return response["choices"][0]["text"] 
    except:
        return "I'm sorry, I don't know the answer."

# Define function to speak text using text-to-speech engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define function to search the web and speak the answer
def search_and_speak(query):
    url = f"https://google.com/search?q={query}"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    answer = soup.select('.hgKElc')[0].text
    speak(answer)

# Define function to open a URL in a specialized browser
def open_in_browser(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

def main(): 
    while True:
        # Wait for user to say "Jarvis" 
        print("Say 'Jarvis' to start recording your question...")
        #speak("Hi siva. i am jarvis, how i can")
        with sr.Microphone() as source: 
            recognizer = sr.Recognizer() 
            audio = recognizer.listen(source) 
            try: 
                transcription = recognizer.recognize_google(audio) 
                if transcription.lower() == "hi jarvis":
                    print("Hi siva, how are you doing?")
                    speak("Hi siva, how are you doing?")
                elif transcription.lower() == "jarvis":
                    # Record audio 
                    filename = "input.wav" 
                    print("Say your question...") 
                    with sr.Microphone() as source: 
                        recognizer = sr.Recognizer() 
                        source.pause_threshold = 1 
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None) 
                        with open(filename, "wb") as f: 
                            f.write(audio.get_wav_data())
                            
                            # Transcribe audio to text 
                            text = transcribe_audio_to_text(filename) 
                            if text:
                                print (f"You said: {text}")
                                
                                # Generate response using GPT-3
                                response = generate_response(text)
                                print(f"GPT-3 says: {response}") 
                                
                                # Read response using text-to-speech 
                                speak(response)
                            else:
                                print("Sorry, I didn't catch that. Could you please repeat?")
                elif transcription.lower() == "search":
                    print("What do you want me to search for?")
                    speak("What do you want me to search for?")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        audio = recognizer.listen(source)
                        try:
                            query = recognizer.recognize_google(audio)
                            print(f"Searching for {query}...")
                            speak(f"Searching for {query}...")
                            url = f"https://www.google.com/search?q={query}"
                            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                            res = requests.get(url, headers=headers)
                            soup = bs4.BeautifulSoup(res.text, 'html.parser')
                            search_results = soup.select('.kCrYT a')
                            for link in search_results[:3]:
                                href = link.get('href')
                                if "url?q=" in href:
                                    result = href.split("?q=")[1].split("&sa")[0]
                                    print(result)
                                    speak(result)
                                    break
                        except:
                            print("Sorry, I didn't catch that. Could you please repeat?")
                elif transcription.lower() == "open":
                    print("What should I open?")
                    speak("What should I open?")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        audio = recognizer.listen(source)
                        try:
                            query = recognizer.recognize_google(audio)
                            if "browser" in query:
                                print("Opening browser...")
                                speak("Opening browser...")
                                subprocess.Popen("C:/Program Files/Microsoft/Edge/Application/msedge.exe")
                            else:
                                print(f"Sorry, I don't know how to open {query}")
                                speak(f"Sorry, I don't know how to open {query}")
                        except:
                            print("Sorry, I didn't catch that. Could you please repeat?")
                elif transcription.lower() == "stop":
                    print("Stopping...")
                    speak("Stopping...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()