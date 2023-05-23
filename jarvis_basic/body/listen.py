import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator#pip install googletrans==3.1.0a0

# Function 1: Listen - Detects and recognizes speech in any language
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
    return query # return query.lower()

# Function 2: English Translation - Translates input text to English
def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text,dest="en").text
    print("You : ", translated_text)
    return translated_text

# Function 3: Connect - Main function to execute the program
# def connect():
#     query = Listen()  # Call the Listen function to get the query

#     if query == "error":
#         print("Error occurred during speech recognition.")
#         return

#     print("Query:", query)

#     if query.isalpha():
#         print("Query is in English.")
#     else:
#         print("Query is in another language. Translating to English...")
#         translated_query = translate_to_english(query)
#         print("Translated Query:", translated_query)

# # Execute the Connect function when the script is run directly
# if __name__ == "__main__":
#     connect()

def MicExecution():
    query = Listen()
    data = translate_to_english(query)
    return data
