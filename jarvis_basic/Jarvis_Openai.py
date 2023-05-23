from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Satring The Jarvis : Wait For Some Seconds")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Satring The Jarvis : Wait For few Seconds")

def MainExcecution():

    Speak("Hello Sivamani")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        try:
            Data = MicExecution()
            Data = str(Data)

            if len(Data)<3:
                pass

            elif "what is" in Data or "where is" in Data or "Question" in Data or "answer" in Data:
                Reply = QuestionAnswer(Data)
                Speak(Reply)
                
            else:
                Reply =ReplyBrain(Data)
                # print(Reply)
                Speak(Reply)
        except:
            print("ERROR")

def ClapDetect():
    query = Tester()
    if "True-mic" in query:
        print("\n>> Clap Detected!! >>\n")
        MainExcecution()
    else :
        pass

ClapDetect()

# def WakeupDetected():
#     query1 = MicExecution()
#     if "wake up" in query1: # os.startfile(r"jarvis_basic\jarvis.py")
#         MainExcecution()
#     else:
#         pass


# while True:
#     WakeupDetected()