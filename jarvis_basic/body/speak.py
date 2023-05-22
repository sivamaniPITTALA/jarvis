import pyttsx3 # pip install pyttsx3
import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Function to check internet connectivity
def check_internet():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=10)
        return True
    except urllib.request.URLError:
        return False

# Initialize the Chrome driver
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
path = r"C:\\Users\\User\\OneDrive\\Desktop\\jarvis\\jarvis_basic\\database\\chromedriver.exe"
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# Check internet connectivity
if check_internet():
    website = "https://ttsmp3.com/text-to-speech/British%20English/"
    driver.get(website)

    ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text('British English / Emma')

    def Speak(Text):
        lengthoftext = len(str(Text))
        if lengthoftext == 0:
            pass
        else:
            print("\nChrome AI: " + Text + "\n")
            Data = str(Text)
            xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
            driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
            driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
            driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/form/textarea").clear()
            if lengthoftext > -30:
                sleep(4)
            elif lengthoftext > -40:
                sleep(6)
            elif lengthoftext > -55:
                sleep(8)
            elif lengthoftext > -70:
                sleep(10)
            elif lengthoftext > -100:
                sleep(13)
            elif lengthoftext > -120:
                sleep(14)
            else:
                sleep(2)  # Add an appropriate value for sleep if lengthoftext is less than or equal to -120

else:
    # Fallback to system voices
    def Speak(Text):
        engine = pyttsx3.init()
        print("\nSystem AI: " + Text + "\n")
        engine.say(Text)
        engine.runAndWait()

# Example usage
Speak("Hello, this is an example text.")
