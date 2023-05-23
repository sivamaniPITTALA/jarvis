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

def QuestionAnswer(question,chat_log = None):
    FileLog = open("jarvis_basic\\Database\\qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 200,
        top_p = 1,#1
        frequency_penalty = 0,#0-1
        presence_penalty = 0,
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("jarvis_basic\\Database\\qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

# while True:
#     kk = input("Enter :")
#     print(QuestionAnswer(kk))
