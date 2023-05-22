from Body.Speak import Speak
from Body.Listen import listen

def MainExe():
    #Speak("Wakeup Detected by Jarvis")
    Speak("Main Execution have been started")
    while True:

        query = listen()

        if "hello" in query:
            Speak("Hello sir, how are you?")    

        elif "bye" in query:
            Speak("Bye sir, Have a nice day") 
            exit()