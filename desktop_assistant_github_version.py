import pyttsx3                                     # It is a text-to-speech conversion library in Python.
import datetime                                    # It provides date and time classes to Python.
import speech_recognition as sr                    # It is used to convert the spoken words into text, make a query or give a reply.
import wikipedia                                   # It is a Python library that makes it easy to access and parse data from Wikipedia.
import webbrowser                                  # It provides a high-level interface that allows displaying Web-based documents to users.
import smtplib                                     # It is an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
import sys                                         # It allows the developer to exit from Python.
import pywhatkit as kt                             # It is a Python Library for scheduling and sending WhatsApp messages with various other functions like playing a video on YouTube, Converting an image to ASCII art, Converting a string to an image with Hand Written Characters etc.
import os                                          # It provides a portable way of using operating system dependent functionality.
import cv2                                         # It is a library of Python bindings designed to solve computer vision problems.
from requests import get                           # It allows us to send 'HTTP' requests using Python.
import winsound                                    # It provides access to the basic sound-playing machinery provided by Windows platforms.
import pyjokes                                     # It uses the get_joke function and drop a random joke into the application.
import pyautogui                                   # It is used to click, drag, scroll, move, etc and it also can be used to click at an exact position.
import requests                                    # It allows us to send HTTP/1.1 requests easily.
import instaloader                                 # It uses to download the posts of public or private account,stories,IGTV,comments on post,profile information,story highlights etc.
import PyPDF2                                      # It is used for splitting, merging, cropping and transforming pages in your PDFs.
from bs4 import BeautifulSoup                      # It is used for web scraping purposes to pull the data out of HTML and XML files.
import speedtest                                   # It is used for testing internet bandwidth using speedtest.net.
from pywikihow import search_wikihow               
import psutil                                      # It is used to access system details and process utilities.
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import time
import random                                     # It generates pseudo random numbers for various given distributions.
from PyQt5 import QtWidgets, QtCore, QtGui        # It is a cross platform GUI toolkit.
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from desktop_assistantUi import Ui_MainWindow

engine = pyttsx3.init('sapi5')                    # It is an application programming interface technology provided by Microsoft for voice recognition and synthesis.
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# Speak Function.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    second = int(datetime.datetime.now().second)
    if hour >= 0 and hour < 12:
        speak("Good Mornning")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon the time is {hour} hours {minute} minutes and {second} seconds")
    elif hour >= 18 and hour < 20:
        speak("Good Evening")
    else:
        speak("Welcome")
    
# Send Email Function.
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Set Alarm Function.

def setAlarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))   
    
    altime = altime[11:-3]
    
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    speak(f"alaram is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                speak("alarm is running")
                winsound.PlaySound('a',winsound.SND_LOOP)
        
        elif Mireal<datetime.datetime.now().minute:
            break
         
# Tell News Function.
                   
def news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey"
    main_page = requests.get(main_url).json()
    article = main_page ["articles"]
    news_article=[]
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
    for arti in article:
        news_article.append(arti['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is {news_article[i]}")
    
# Read PDF Function.
        
def pdf_reader():
    file_path = r'E:\\Python Project\\AI Assistant version 1.0.0\\lesson.pdf'
    book=open(file_path,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"this book has total {pages} pages")
    speak("which page you want me to read master")
    pg=int(input("please enter the page number"))
    speak(f"ok I am reading the {pg} page")
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak(text)
   
# Send WhatsApp Message Function.
   
def watsapp_Msg(name,message):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=169, y=110)
    sleep(5)
    write(name)
    sleep(5)
    click(x=168, y=233)
    sleep(5)
    click(x=611, y=695)
    sleep(5)
    write(message)
    press('enter')
    
# Find WhatsApp Contact Info Function.
    
def contact_info(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15)
    click(x=169, y=110)
    sleep(2)
    write(name)
    sleep(2)
    click(x=168, y=233)
    sleep(2)
    click(x=471, y=60)
    sleep(2)
    
# Make WhatsApp Video Call Function.
    
def watsapp_videoCall(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=169, y=110)
    sleep(5)
    write(name)
    sleep(5)
    click(x=168, y=233)
    sleep(5)
    click(x=611, y=695)
    sleep(5)
    click(x=1156, y=54)
    
# WhatsApp Open Chat Function.
    
def watsapp_openchat(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15)
    click(x=169, y=110)
    sleep(2)
    write(name)
    sleep(2)
    click(x=168, y=233)
    sleep(2)
    
# Make WhatsApp Voice Call Function.
    
def watsapp_Call(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=169, y=110)
    sleep(5)
    write(name)
    sleep(5)
    click(x=168, y=233)
    sleep(5)
    click(x=611, y=695)
    sleep(5)
    click(x=1207, y=53)

# Countdown Timer Function.

def countdownTimer(user_time):
    user_time = user_time.replace("set a timer for", "")
    user_time = user_time.replace("minutes", "")
    user_time = int(user_time)
    user_time = (user_time * 60)
    speak("Timer is set successfully")
    while user_time > 0:
        print(user_time)
        user_time = user_time -1
        time.sleep(1)
        if user_time == 0:
            speak("Master time is up")
  
# Send Message in Facebook Messenger Function.
  
def facebookmessanger_Msg(name,message):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\Programs\\Messenger\\Messenger.exe")
    sleep(15)
    click(x=448, y=113)
    sleep(5)
    write(name)
    sleep(5)
    press_and_release('Ctrl+1')
    sleep(5)
    click(x=778, y=696)
    sleep(5)
    write(message)
    press('enter')

# Make voice call through Facebook Messenger Function.
  
def facebookmessanger_Voice_call(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\Programs\\Messenger\\Messenger.exe")
    sleep(15)
    click(x=448, y=113)
    sleep(5)
    write(name)
    sleep(5)
    press_and_release('Ctrl+1')
    sleep(5)
    click(x=778, y=696)
    sleep(5)
    click(x=1051, y=55)  
   
# Make video call through Facebook Messenger Function.
    
def facebookmessanger_Video_call(name):
    startfile("C:\\Users\\Suvro\\AppData\\Local\\Programs\\Messenger\\Messenger.exe")
    sleep(15)
    click(x=448, y=113)
    sleep(5)
    write(name)
    sleep(5)
    press_and_release('Ctrl+1')
    sleep(5)
    click(x=778, y=696)
    sleep(5)
    click(x=1087, y=56)
  
class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        speak("Please say wake up to continue further")
        while True:
            self.query = self.takecomand().lower()
            if 'wake up' in self.query:
                self.taskExecution()

    # Take Command Function.

    def takecomand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Please say again....")
            return "none"
        return query

    # Task Execution / performing Function.

    def taskExecution(self):
        speak("Hello Master")
        wishMe()
        speak("Hope you are fine")
        speak("I am your AI assistant")
        
        while True:
        
            self.query = self.takecomand().lower()

            # Search content from wikipedia.

            if 'search wikipedia' in self.query:
                speak("What do you want to search")
                self.query = self.takecomand().lower()
                speak('Please wait searching Wikipedia....')
                self.query = self.query.replace("in wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia....")
                speak(results)
               
            # Search content using browser.
                
            elif 'can you answer me something' in self.query:
                speak('yes , I am here to help you out')
                while True:
                    speak('please ask me what do you want to know')
                    self.query = self.takecomand().lower()
                    speak(f"Here is your answer{self.query}")
                    try:
                        if 'ok close' in self.query:
                            speak("ok closing for now but feel free to ask me anything")
                            break
                        else:
                            max_result = 1
                            how_to = search_wikihow(self.query, max_result)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry due to slow internet connection I am not able to answer your question")
             
            # Search content from youtube.
                        
            elif 'open youtube' in self.query:
                speak("What should I search in youtube")
                search = self.takecomand().lower()
                speak("Please wait searching in youtube")
                kt.playonyt(f"{search}")
                
            # Search content from google.

            elif 'open google' in self.query:
                speak("What should I search?")
                question = self.takecomand().lower()
                speak('Please wait searching in google.')
                webbrowser.open(f"{question}")
                
            # Check the running train status with input of train number given by the user.
            
            elif 'check my train status' in self.query:
                speak("Ok master, but before that I want you to enter the train number correctly")
                train_number = input("Enter the tain number here....")
                webbrowser.open("https://www.railyatri.in/")
                sleep(10)
                click(x=485, y=204)
                sleep(5)
                write(train_number)
                press('enter')
                sleep(5)
                speak("Here is your result")
                
            # Check the PNR status with input of PNR number given by the user.
            
            elif 'check my pnr status' in self.query:
                speak("Ok master, but before that I want you to enter your pnr number correctly")
                pnr_number = input("Enter your pnr number here....")
                webbrowser.open("https://www.railyatri.in/")
                sleep(10)
                click(x=376, y=194)
                sleep(5)
                click(x=485, y=204)
                sleep(5)
                write(pnr_number)
                press('enter')
                sleep(5)
                speak("Here is your result")
            
            # Tells how is the system and asks how is the user.
                
            elif 'how are you' in self.query:
                speak("Thanks for asking, I am doing absoutely fine")
                speak("What about you Master")
        
            # Tells about the gender.
        
            elif 'what is your gender' in self.query:
                speak("I don't have any, suvro created me")
                
            # Opens the visual studio code.
                
            elif 'open code' in self.query:
                codepath = "C:\\Users\\Suvro\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
             
            # Closes the visual studio code.
                
            elif 'close code' in self.query:
                speak("Ok suvro closing code")
                os.system("taskkill /f /im Code.exe")
              
            # Opens the notepad.
                
            elif 'open notepad' in self.query:
                notepadpath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(notepadpath)
            
            # Closes the notepad.
                
            elif 'close notepad' in self.query:
                speak("Ok suvro closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # Tells about the IP Address.

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Master, your IP address is {ip}")
             
            # Tells about the Screen Size.
                
            elif 'screen size' in self.query:
                screen_size = pyautogui.size()
                speak(f"Your current screen resolution width and height is{screen_size}")
              
            # Tells about the time.
                
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Master, the time is {strTime}")
                
            # Shuts down the system.
                
            elif 'shutdown' in self.query:
                os.system("shutdown /s /t 5")
              
            # Restarts the system.
                
            elif 'restart' in self.query:
                os.system("shutdown /r /t 5")
                
            # Turns on the sleep mode.
            
            elif 'sleep mode' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                
            # Turns the volume up.
                
            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
             
            # Turns the volume down.
                
            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
                
            # Mute the system.
                
            elif 'mute' in self.query:
                pyautogui.press("volumemute")
                
            # Unmute the system.
                
            elif 'unmute' in self.query:
                pyautogui.press("volumeunmute")
                
            # Plays songs randomly from a specified directory.
            
            elif 'play songs for me' in self.query:
                music_dir = ("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\sample_songs")
                songs = os.listdir(music_dir)
                random_songs = random.choice(songs)
                os.startfile(os.path.join(music_dir,random_songs))

            # Switch between working windows.
                
            elif 'switch between windows'in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
               
            # Tells about the battery percentage.
                
            elif 'battery percentage' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"The system has {percentage} percent battery")
                if percentage>= 75:
                    speak("The system has enough power to continue to work")
                elif percentage >= 40 and percentage < 75:
                    speak("Connect the system with a charging station")
                elif percentage >= 15 and percentage <= 30:
                    speak("The system can't run with this power")
                elif percentage <= 75:
                    speak("The system is going to shut down")
                  
            # Tells about the internet speed.
                    
            elif 'internet speed' in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak("checking your internet speed")
                speak(f"your downloading speed is {dl} bit per second and your uploading speed is {up} bit per second")
                
            # Takes note for the user.
                
            elif 'take notes for me' in self.query:
                speak("Ok, but what should I note master")
                note = self.takecomand()
                remember = open("data.txt",'w')
                remember.write(note)
                remember.close()
                speak("I have noted" + note)
            
            # Tells the user about the saved notes or checklists if any.
            
            elif 'tell my checklist' in self.query:
                speak("Checking master")
                remember = open("data.txt",'r').read()
                speak("You have told me to remember you that" + remember)
             
            # Takes screenshot and saves that in system for the user.    
             
            elif 'take a screenshot'in self.query:
                speak("tell me the name for the screeshot file")
                name = self.takecomand().lower()
                speak("please hold the screen for few seconds, so that i can take screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot taken and saved successfully")
               
            # Read saved pdf for the user.
                
            elif 'read book'in self.query:
                pdf_reader()       

            # Opens linkedIn for the user.
            
            elif 'open linkedin' in self.query:
                webbrowser.open("https://www.linkedin.com/in/name-surname-942031ab/")
                 
            # Send WhatsApp Messages.
                    
            elif 'send message to' in self.query:
                name = self.query.replace("send message to", "")
                name = str(name)
                speak("What is your message")
                message = self.takecomand()
                watsapp_Msg(name,message)
                speak("Message sent successfully")
             
            # Search Contact Information using WhatsApp.
                
            elif 'search contact information' in self.query:
                name = self.query.replace("search contact information of", "")
                contact_info(name)
                speak("Here is your information")
             
            # Make video call using WhatsApp.
                
            elif 'make a video call to' in self.query:
                name = self.query.replace("make a video call to", "")
                watsapp_videoCall(name)
                speak("Enjoy your moment")
             
            # Make voice call using WhatsApp.  
                
            elif 'make a call to' in self.query:
                name = self.query.replace("make a call to", "")
                watsapp_Call(name)
                speak("Enjoy talking")
             
            # Opens personalise chat using WhatsApp.
                
            elif 'open my chat with' in self.query:
                name = self.query.replace("open my chat with", "")
                watsapp_openchat(name)
                speak("Here is your chat buddy")
        
            # Opens Camera.
          
            elif 'open camera' in self.query:
                cam = cv2.VideoCapture(0)
                cv2.namedWindow("Python Webcam")
                img_counter = 0
                while True:
                    ret, frame = cam.read()
                    
                    if not 'ret':
                        speak("Failed to grab frame")
                        break
                    
                    cv2.imshow('webcam',frame)
                    K = cv2.waitKey(1)
                    if K % 256 == 27:
                        speak("Escape hit")
                        break
                    
                    elif K % 256 == 32:
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name,frame)
                        speak("Image captured")
                        img_counter+=1
                        break
                cam.release()
                cv2.destroyAllWindows()

            # Sends Email.

            elif 'send an email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takecomand()
                    to = "receiver'semail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent successfully!")
                except Exception as e:
                    print(e)
                    speak("Sorry Master!I am unable to sent the email")
                
            # Send Message through Facebook Messenger.   
                    
            elif 'send message in messenger to' in self.query:
                name = self.query.replace("send message in messenger to", "")
                name = str(name)
                speak("What is your message")
                message = self.takecomand()
                facebookmessanger_Msg(name,message)
                speak("Message sent successfully")
            
            # Make voice call through Facebook Messenger.
            
            elif 'make call in messenger to' in self.query:
                name = self.query.replace("make call in messenger to", "")
                name = str(name)
                speak("Please wait a moment suvro")
                facebookmessanger_Voice_call(name)
                speak("Enjoy Talking Suvro")
            
            # Make video call through Facebook Messenger.
            
            elif 'make a video call in messenger to' in self.query:
                name = self.query.replace("make a video call in messenger to", "")
                name = str(name)
                speak("Please wait a moment suvro")
                facebookmessanger_Video_call(name)
                speak("Enjoy Talking Suvro")

            # Sets Alarm.
            
            elif 'set alarm' in self.query:
                speak("for what time you want me to set the alram, for example, set alarm to 5:30 am")
                tt = self.takecomand()
                tt = tt.replace("set alarm to ","")
                tt = tt.replace(".","")
                tt = tt.upper()
                setAlarm(tt)
            
            # Tells Joke.
             
            elif 'tell me jokes' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            # Tells Current News.
                
            elif 'tell me news' in self.query:
                speak("Please wait while searching for latest news for you")
                news()
              
            # Finds the device's location using IP Address.
                
            elif 'find me' in self.query:
                speak("please wait let me check once")
                try:
                    ip_address = get('https://api.ipify.org').text
                    url = ('https://get.geojs.io/v1/ip/geo/')+ ip_address +('.json')
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"I am not sure, but I think you are in {city} city of country {country}")
                except Exception as e:
                    speak("sorry master I am not able to find your location due to poor network connection")
                    pass
              
            # Opens the Instagram profile of the user and if instructed download the profile picture as well.
                
            elif 'open my instagram profile'in self.query:
                speak("please enter the user name correctly")
                name = input("Enter your user name here....")
                webbrowser.open(f"https://www.instagram.com/{name}")
                time.sleep(10)
                speak("wao your profile picture looks great, would you like to download and save that in your system")
                condition = self.takecomand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I have downloaded and saved the picture successfully in your device")
                else:
                    speak("as u wish")
              
            # Opens the Facebook profile of the user.
                    
            elif 'open my facebook profile'in self.query:
                speak("please enter the user name correctly")
                name = input("Enter your user name here....")
                password = input("Enter your password here....")
                webbrowser.open(f"https://www.facebook.com//{name}{password}")
                speak("Enjoy faceboook suvro")

            # Hide and Unhide the files or folders of the system from a particular directory.

            elif 'hide my files' in self.query or 'visible my files' in self.query:
                speak("Please confirm me once again do you realy want to hide the files or make the visible to everyone")
                condition = self.takecomand().lower()
                if 'hide' in condition:
                    os.system("attrib +s +h /s /d")
                    speak("All your files are hidden successfully")
                if 'visible' in condition:
                    os.system("attrib -s -h /s /d")
                    speak("All your files are visible to everyone")
               
            # Tells Current Temperature.
                    
            elif 'temperature' in self.query:
                search = "temperature in kolkata"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current{search} is {temp}")
                
            # Sets timer for the user.
                
            elif 'set a timer for' in self.query:
                user_time = self.takecomand().lower()
                countdownTimer(user_time)
                
            # Says goodbye to the user and closes the loop as well.
                
            elif 'goodbye' in self.query:
                speak("goodbye Suvro,thanks for using me")
                break
   
startExecution = MainThread()
   
class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.RUN.clicked.connect(self.startTask)
        self.gui.TERMINATE.clicked.connect(self.close)
        self.gui.WatsApp.clicked.connect(self.WatsApp_app)
        self.gui.Facebook.clicked.connect(self.Facebook_app)
        self.gui.YouTube.clicked.connect(self.Youtube_app)
        self.gui.Google.clicked.connect(self.Google_app)
    
    def Google_app(self):
        
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
    def Facebook_app(self):
            
        webbrowser.open("https://www.facebook.com/")
        
    def Youtube_app(self):
            
        webbrowser.open("https://www.youtube.com/")
    
    def WatsApp_app(self):
        
        os.startfile("C:\\Users\\Suvro\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        
    def startTask(self):
        
        self.gui.label1 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\bot_templete.gif")
        self.gui.bot_templete.setMovie(self.gui.label1)
        self.gui.label1.start()
        
        self.gui.label2 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\system_online.gif")
        self.gui.system_online.setMovie(self.gui.label2)
        self.gui.label2.start()
        
        self.gui.label3 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\smart_match.gif")
        self.gui.smart_match.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        self.gui.label4 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\initial.gif")
        self.gui.initialgif.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        self.gui.label5 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\Code_Template.gif")
        self.gui.Code_Templete.setMovie(self.gui.label5)
        self.gui.label5.start()
        
        self.gui.label6 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\Earth_Template.gif")
        self.gui.Earth_Templete.setMovie(self.gui.label6)
        self.gui.label6.start()
        
        self.gui.label7 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\Jarvis_Gui (1).gif")
        self.gui.Jarvis_Gui.setMovie(self.gui.label7)
        self.gui.label7.start()
        
        self.gui.label8 = QtGui.QMovie("E:\\Python Project\\AI Assistant\\AI Assistant version 1.1.1\\G.U.I Material\\Background\\standing_bot.gif")
        self.gui.standing_bot.setMovie(self.gui.label8)
        self.gui.label8.start()
        
        startExecution.start()
        
app = QApplication(sys.argv)
desktop_assistant = Main()
desktop_assistant.show()
exit(app.exec_())