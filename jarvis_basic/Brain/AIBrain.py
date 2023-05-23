#Open AI
fileopen = open("jarvis_basic\\Data\\Api.txt")
API = fileopen.read()
fileopen.close()
# print(API)
import openai # pip install openai
from dotenv import load_dotenv # pip3 install python-dotenv

#Open AI coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    FileLog = open("jarvis_basic\\Database\\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 100,
        top_p = 0.3,#1
        frequency_penalty = 0.5,#0-1
        presence_penalty = 0,
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("jarvis_basic\\Database\\chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

# reply = ReplyBrain("Hello, How are you?")
# print(reply)

# while True:
#     kk = input("Enter :")
#     print(ReplyBrain(kk))
