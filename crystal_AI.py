import pyttsx3
from apikey import api_data
import openai
from pynput.keyboard import Key, Controller              # PROJECT CRYSTAL
import speech_recognition as sr                          
import datetime
import os
import cv2
import requests
from requests import get
import wikipedia
import webbrowser
import keyboard
import sys
import urllib
from urllib.request import urlopen
import time
from plyer import notification
import screen_brightness_control as pct
import pyautogui

openai.api_key=api_data

completion=openai.Completion()




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',185)


def Reply(question):
    prompt=f'Kowshal: {question}\n Crystal: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Kowshal'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

def speak1(text):
    engine.say(text)
    engine.runAndWait()

def check():
    import socket
    import time
    import os
    
    net=1
    os.system('TASKKILL /F /IM cmd.exe')
    while True:
     try:
        socket.create_connection(('Google.com',80),timeout=5)
        speak("Internet connection is active, initializing your personal voice assistant")
        
        
        time.sleep(2)
        wake()
        
     except OSError:
        import time
        tim=50
        print("no internet")
        if net==1:
            speak("System is offline, You need internet to interact with Crystal AI")
        elif net==tim:
            net=0
            
        net=net+1
        time.sleep(2)



# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



# voice to text
def takecommand4():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("lisening...")
        r.pause_threshold = 3
        audio = r.listen(source,timeout=50,phrase_time_limit=3)


    try:
         print("recognising..")
         query = r.recognize_google(audio, language='en-in')
         print(f"You said: {query}")


    except Exception as e:
        print(" Say that again please...")
        return "none"
    return query

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("you Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query
def takecommand1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("you Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query

def takecommand2():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("lisening...")
        r.pause_threshold = 3
        audio = r.listen(source,timeout=50,phrase_time_limit=5)


    try:
         print("recognising..")
         query = r.recognize_google(audio, language='en-in')
         print(f"You said: {query}")


    except Exception as e:
        print(" Say that again please...")
        return "none"
    return query


        

def wake():
     notification.notify(
            title = "Crystal",
            message = "Crytal AI is Online!",
            app_icon = "C:\\icon\\ai.ico",
            app_name = "Crystal AI",
            timeout=5
            )
     speak("Hey there! your assistant is online")
     
     while True:
      query = takecommand().lower()
      if "hello" in query or "hey crystal" in query:
       

       wish()

def hotword():
    while True:

        query = takecommand().lower()
        if "wakeup" in query or "wake up" in query or "hey crystal" in query or "hello crystal" in query:
            wish()

             


def c():
    
    speak(" Starting C automation, Sir this feature is still in development, So you may find some bugs")
    os.startfile("C:\TURBOC3\Turbo C++\Turbo C++.exe")
    auto()
def auto():
    import keyboard
    time.sleep(2)
    keyboard.press_and_release('enter')
    
    speak("sir, shall i start new project")
    query = takecommand().lower()
    if "okay" in query or "ok" in query or "sure" in query:
            keyboard.press_and_release('shift+f')
            keyboard.press_and_release('shift+n')
    speak(" Now you have to guide me what to write, sir")
    while True:
        query = takecommand().lower()
        ans=Reply(query)
        print(ans)
        if "use basic header file" in query or "use basic headerfile in query":
              speak("oaky")
              c="include"
              d="iostream.h"
              keyboard.press_and_release('shift+3')
              for char in f"{c}":
                  keyboard.press(char)
                  keyboard.release(char)
                  keyboard.press_and_release('shift+comma')
              for char in f"{d}":
                  keyboard.press(char)
                  keyboard.release(char)
                  keyboard.press_and_release('shift+dot')
                  keyboard.press_and_release('enter')
              c="include"
              d="conio.h"
              keyboard.press_and_release('shift+3')
              for char in f"{c}":
                  keyboard.press(char)
                  keyboard.release(char)
                  keyboard.press_and_release('shift+comma')
              for char in f"{d}":
                  keyboard.press(char)
                  keyboard.release(char)
              keyboard.press_and_release('shift+dot')

     


              

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
         speak("good morning sir, what can i do for you")
    elif hour>12 and hour<18:
         speak("good afternoon sir, what can i do for you")
    else:
          speak("good evening sir, what can i do for you")
         
    
    i=1
    loop=1
    off=0
    while True:
     import keyboard
     loop=loop+1
     x=10
     little=50
     import psutil
     battery =psutil.sensors_battery()
     per = battery.percent
     plug = battery.power_plugged 
     cpu = psutil.cpu_percent(interval=1)
     ruse = psutil.virtual_memory().percent
      
     if off==100:
           import sys
           sys.exit 
       
     if per < 20 and plug==False:
           speak(" laptop has reached below 20 percent, Iam hibernating the laptop")
           notification.notify(
            title = "Crystal",
            message = "hibernating laptop",
            app_icon = "D:\\icon\\ai.ico",
            timeout=3
            )
           os.system("shutdown -h")
           hotword()
     if per < 30 and plug==False:
           speak("sir, the battery is below 30 percent, if the battery reaches below 20 percent i will automatically hibernate the laptop")
     if per < 30 and plug==True:
           print("charging")
     if ruse > 85:
           speak(" The ram usage has reached above 85 percent, Iam hibernating the laptop")
           notification.notify(
            title = "Crystal",
            message = "hibernating laptop",
            app_icon = "D:\\icon\\ai.ico",
            timeout=3
            )
           os.system("shutdown -h")
           hotword()               
     if ruse > 70:
           speak(" Sir, ram usage has exceeded above 70 percent, if it exceeds above 85 percent i will hibernate the laptop")
     if loop ==1 and cpu > 70:
         loop=loop+1  
         speak("sir, the CPU usage has exceeded 70 percent, this may effect laptop peformance");

     if loop==5 and cpu > 70:
            loop=1
            notification.notify(
            title = "Crystal",
            message = "hibernating laptop",
            app_icon = "D:\\icon\\ai.ico",
            timeout=3
            )
            os.system("shutdown -h")
            hotword()
              
         
     else:
         
         
         
     
       
       query = takecommand().lower()
       if "help me to write to write program" in query or "start c automation" in query or "start C automation" in query or "start se automation" in query: 
           c()
       if "cpu peformance" in query or "cpu status" in query or "cpu health" in query:
           import psutil
           cpu = psutil.cpu_percent(interval=1)
           speak(f"sir, currently cpu is at {cpu} percent usage")

       elif "change screen brightness for zero" in query:
           pct.set_brightness(0)
       elif "change screen brightness for hundred" in query or "change screen brightness for android" in query:
           pct.set_brightness(100)   
       elif "change screen brightness for" in query:
         try:
           import keyboard
           cm = query.replace("change screen brightness for"," ")
           for char in f"{cm}":
               pct.set_brightness(cm)
           speak("is this enough sir")
         except:
             speak("i did not understand sir") 
       elif "change screen brightnes" in query:
           speak("How much should i change sir?")
           query=takecommand().lower()
           if "low" in query or "less" in query or "down" in query:
               bright=little-100
               pct.set_brightness(bright)
               little=little-10
           elif "high" in query or "more" in query or "up" in query:
               bright=little+10
               pct.set_brightness(bright)
               little=little+10    
               
       elif "ram usage" in query or "ram status" in query or "memory usage" in query or "memory status" in query:
           ruse = psutil.virtual_memory().percent
           speak(f" Ram usage is at {ruse} percent")
       elif "ram size" in query or "installed ram" in query or "total ram" in query:
           speak(f"total ram is{round(psutil.virtual_memory().total/1000000000,1)} gigabyte")
       elif "open notepad" in query:
          npath = "C:\\Windows\\system32\\notepad.exe"
          speak(" opening Notepad for you")
          os.startfile(npath)
       elif "open command prompt" in query:
            speak(" opening Command prompt for you")
            os.system("start cmd")
       elif "ssd stat" in query or "free space do i have" in query or "disk space" in query:
           import shutil

           total, used, free = shutil.disk_usage("/")

           speak("Total size of your ssd is  %d GigaByte" % (total // (2**30)))
           speak("Used space is  %d GigaByte" % (used // (2**30)))
           speak("and Free space is  %d GigaByte" % (free // (2**30)))
       
       elif "gaming mode" in query or "performance mode" in query or "system in gaming mode" in query:
           speak("Optimising system for gaming in 3, 2, 1")
           os.system('powercfg -setactive fe0570d3-7990-487e-ac5c-3112c0b1e38e')
           speak("power config set to Gaming mode")
           notification.notify(
            title = "Crystal",
            message = "Gaming Mode Enabled",
            app_icon = "C:\\icon\\gaming.ico",
            timeout=3
            )
           bright=100
           pct.set_brightness(bright)
           cpu = psutil.cpu_percent(interval=1)
           speak("Screen brightness set to 100")
           
           ruse = psutil.virtual_memory().percent
           speak(f"The the RAM is set to {ruse} percent usage and CPU to {cpu} percent")
           
       elif "battery saving mode" in query or "save battery" in query:
           os.system('powercfg -setactive afdcf2ec-833b-4260-a313-ed1d1adac42c')
           notification.notify(
            title = "Crystal",
            message = "Battery Saving Mode Enabled",
            app_icon = "C:\\icon\\battery.ico",
            timeout=3
            )
           speak("Power config set to power saving mode")
       elif "balanced mode" in query or "balance mode" in query:
           os.system('powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e')
           notification.notify(
            title = "Crystal",
            message = "Balanced Mode Enabled",
            app_icon = "C:\\icon\\ai.ico",
            timeout=3
            )
           speak("Power config set to Balanced mode")
           

       elif "system status" in query or "system peformance" in query or "how is the system" in query or "how is the sister" in query or "system" in query:
           battery =psutil.sensors_battery()
           per = battery.percent
           plug = battery.power_plugged 
           cpu = psutil.cpu_percent(interval=1)
           ruse = psutil.virtual_memory().percent
           speak("checking system")
           if plug== True:
               speak(f" System is currently charging and the battery is at {per} percent")
           else:
               speak(f" System is running on battery and level is at {per} percent ")
           if per >= 90 and plug == False:
               speak(" I think the battery level is great and lasts long ")
           elif per >= 60 and plug == False:
               speak(" I think the battery is doing fine, lasts about an hour ")
           elif per >=40 and plug== False:
               speak(" Battery may lasts about half an hour")
           elif per < 40 and plug == False:
               speak(" Sir, the battery is at critical condition, please plug in the charger")
           speak(f" Currently the CPU is at {cpu} percent utilization and the RAM is at {ruse} percent usage")
           bright = pct.get_brightness()
           speak(f" Screen brightness is at {bright} percent")
       
       elif "increase volume" in query or "can you speak loud" in query or "volume up" in query or "i cannot hear you" in query or "i can't hear you" in query:
         
            
           pyautogui.press("volumeup")
           speak("is this enough")
       elif "decrease volume" in query or "volume down" in query or "your too loud" in query or "you are too loud" in query:
           pyautogui.press("volumedown")
           speak("is this enough")
       elif "mute system" in query or "mute yourself" in query:
           pyautogui.press("volumemute")
           speak("is this enough")
       elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")


       elif "wikipedia" in query:
           speak(" Searching wikipedia....")
           query = query.replace("wikipedia"," ")
           results = wikipedia.summary(query, sentences=2)
           speak(" sir , according to wikipedia")
           speak(results)
           print(results)

       elif "open youtube" in query:
           speak(" opening youtube on chrome")
           webbrowser.open("www.youtube.com")

       elif "can you search for me" in query:
           speak(" Sir , what should i search for!")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")

       elif "search a video on youtube" in query:
           import pywhatkit as kit
           speak(" can you say the name of the video sir?")
           cm = takecommand().lower()
           kit.playonyt(f"{cm}")

       elif "go offline" in query or "go f*** yourself" in query or "f*** off" in query:
           import sys
           speak(" ok sir! going offline ")
           notification.notify(
            title = "Crystal",
            message = "Crystal AI is offline",
            app_icon = "D:\\icon\\ai.ico",
            timeout=5
            )
           
           sys.exit()
           
           

       elif "i will call you back" in query or "wait in background" in query or "wait for me in background" in query or "i call you back" in query or "stay in background" in query or "stay in the background" in query:
           speak(" As you wish sir, i will wait for you in background, just say hello crystal , or wakeup ")
           hotword()


       elif "introduce yourself" in query or "who is your creator" in query or "who is your father" in query:
           speak(" Iam Crystal , iam your virtal assistant and a good A I built by Kowshal. iam an advance A I built for this purticular system. I was created on july 20 2021. I can do whatever the tasks you give me. If you want to know  more just say what you can do! ")        

       elif "what can you do" in query or "what you can do" in query or "i need your help" in query:
           speak(" i can do lot more things you can imagine. I can open certain applications like paint, notepad etc. I can search what ever you want from internet. i can play videos on youtube. i can close or kill applications. I can search from wikipedia and say it to you ")  

       elif "close notepad" in query:
           speak(" closing notepad ")
           os.system('TASKKILL /F /IM notepad.exe')
       elif "close command prompt" in query:
           speak(" closing command prompt ")
           os.system('TASKKILL /F /IM cmd.exe')

       elif "open this pc" in query:
           speak(" opening this PC")
           os.system('explorer.exe')

       elif "who am i" in query or "do you know me" in query or "what is my name" in query:
           speak(" You are Kowshal, the person who built me. You are the reason for my existence")
            


       elif "create a folder" in query:
           speak(" can you specify the drive location, say the name like local disk , game drive or personal drive ")
           query = takecommand().lower()
           if "d" in query or "D" in query or "d drive" in query or "D drive" in query or "game drive" in query:
                 path = "D:/"
                 speak(" what should i name the folder, sir?")
                 cm = takecommand().lower()
                 path = f"D:/{cm}"
                 os.mkdir(path)
                 speak(" folder created, sir")
           elif "c" in query or "C" in query or "c drive" in query or "C drive" in query or "local disk" in query:
                 path = "C:/"
                 speak(" what should i name the folder, sir?")
                 cm = takecommand().lower()
                 path = f"C:/{cm}"
                 os.mkdir(path)
                 speak(" folder created, sir")
           elif "e" in query or "E" in query or "e drive" in query or "E drive" in query or "personal drive" in query:
                 path = "E:/"
                 speak(" what should i name the folder, sir?")
                 cm = takecommand().lower()
                 path = f"E:/{cm}"
                 os.mkdir(path)
                 speak(" folder created, sir")

       elif "open control panel" in query or "open control pannel" in query:
          speak(" ok sir! opening control panel")
          os.system('cmd /c control')
       elif "can you type for me" in query or "just type what I say" in query:
          import keyboard
          import time
          speak("what should i type sir?")
          value = takecommand1().lower()
          for char in f"{value}":
           keyboard.press_and_release(char)
           time.sleep(0.09)
          
       elif "thanks" in query or "thank you" in query or "thankyou" in query:
              speak("Its my pleasure, sir. My job is to help you and make things easy for you")

       elif "open chrome" in query:
           path = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
           speak(" ok i will open chrome")
           os.startfile(path)

       elif "open turbo c" in query or "open c++" in query:
           path = "C:\\TURBOC3\\Turbo C++\\Turbo C++.exe"
           speak(" as you wish")
           os.startfile(path)
       elif "what is the battery status" in query or "how is the battery doing" in query or "how much power do we have" in query or "battery status" in query or "power level" in query:
          import psutil
          battery =psutil.sensors_battery()
          percentage = battery.percent
          speak(f" Battery is at {percentage} percent, sir")
       elif "close control panel" in query: 
          os.system('TASKKILL /F /IM control')
          speak("as you wish sir")
          

       elif "nothing" in query or "no" in query or "get lost" in query or "leave me alone" in query or "no thanks" in query:
            i=i+1    
            if i == x:
             speak(" I hope you are fine , by the way if you need me just say hello crystal, or wakeup ")
             hotword()

       elif "open c drive" in query or "open local disk" in query:
           path = "C:\\"
           speak(" as you wish")
           os.startfile(path)

       elif "open h drive" in query or "open copy drive" in query:
           path = "H:\\"
           speak(" as you wish")
           os.startfile(path)

       elif "open d drive" in query or "open game drive" in query:
           path = "D:\\"
           speak(" as you wish")
           os.startfile(path)

       elif "open e drive" in query or "open personal drive" in query:
           path = "E:\\"
           speak(" as you wish")
           os.startfile(path)
       elif "open folder" in query or "open file" in query:
           import keyboard
           speak("can you say the name sir?")
           cm = takecommand().lower()
           for char in f"{cm}":
               keyboard.press_and_release(char)
           keyboard.press_and_release('enter')

       elif "go back" in query or "open previous folder" in query:
           import keyboard
           keyboard.press_and_release('backspace')

       elif "scroll down" in query or "go down" in query:
           import keyboard
           keyboard.press_and_release('page down')

       elif "scroll up" in query or "go up" in query:
           import keyboard
           keyboard.press_and_release('page up')

           
           
       
       elif "open python"in query:
          path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\pythonw.exe"
          speak("opening python")
          os.startfile(path)
       elif "open python shell"in query:
          path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
          speak("opening python shell")
          os.startfile(path)

       elif "open virtual box"in query or "open virtualbox" in query:
          path = "E:\\vmware\\VirtualBox.exe"
          speak("opening oracle virtual box")
          os.startfile(path)

       elif "close virtual box"in query or "close virtualbox" in query:
          os.system('TASKKILL /F /IM VirtualBox.exe')
          speak("as you wish")
            
          
       elif "close browser" in query:
          speak(" closing internet explorer ")
          os.system('TASKKILL /F /IM iexplore.exe')


       elif "close turbo c" in query or "open c++" in query:
          speak("sorry, i cannot close DOS based programs")


       elif "close chrome" in query:
           speak("closing chrome")
           os.system('TASKKILL /F /IM chrome.exe')

       elif "shut down in a minute" in query or "shutdown in a minute" in query or "shut down system in a minute" in query or "shutdown system in a minute" in query:
           speak("OK. shutting system in 1 minute")
           os.system('shutdown -s -t 60')

       elif "abort system shutdown" in query or "dont shut down system" in query or "do not shutdown" in query or "abort system shut down" in query or "cancel system shutdown" in query or "cancel system shut down" in query or "abort shutdown" in query or "cancel shutdown"in query:
           os.system('shutdown -a')
           speak(" as you wish sir. Aborting shutdown !!")
           
          

       elif "list folders of local disk" in query or "list folders of c drive" in query or "list folders of C drive" in query:
           
               speak(" listing all directory of local disk")
               ls = os.listdir('c:/')
               speak(f" directories are {ls}")

       elif "list folders of game drive" in query or "list folders of d drive" in query or "list folders of D drive" in query:
           
               speak(" listing all directory of game drive")
               ls = os.listdir('d:/')
               speak(f" directories are {ls}")


       elif "list folders of personal drive" in query or "list folders of e drive" in query or "list folders of E drive" in query:
           
               speak(" listing all directory of game drive")
               ls = os.listdir('d:/')
               speak(f" directories are {ls}")
               
       elif "switch tab" in query or "previous tab" in query or "tab" in query or "switch window" in query:
           
           
           keyboard.press('alt + tab')
           keyboard.release('alt + tab')



       elif "select all" in query:
           import keyboard
           import time
           speak("ok")
           keyboard.press('ctrl + a')
           time.sleep(0.5)
           keyboard.release('ctrl + a')


       elif "copy" in query or "copy it" in query or "copy selected" in query:
           import keyboard
           import time
           speak("coppied")
           keyboard.press('ctrl + c')
           time.sleep(0.5)
           keyboard.release('ctrl + c')


       elif "paste" in query or "paste it" in query:
           import keyboard
           import time
           speak("ok sir")
           keyboard.press('ctrl + v')
           time.sleep(0.5)
           keyboard.release('ctrl + v')

       elif "save" in query or "save it" in query:
           import keyboard
           speak(" As you wish , sir")
           keyboard.press_and_release('ctrl + s')


       elif "lock system" in query:
           speak("as you wish, sir")
           os.system('rundll32.exe user32.dll,LockWorkStation')



       elif "turn on system" in query:
           import keyboard
           speak(" okay !")
           keyboard.press_and_release('enter')

       elif "open task manager" in query:
           import keyboard
           speak("as you wish sir")
           keyboard.press_and_release('ctrl + shift + esc')

       elif "open group policy" in query or "open local group policy" in query:
           import keyboard
           import time
           speak(" I will do that for you ! ")
           keyboard.press_and_release('windows + r')
           time.sleep(0.08)
           for char in "gpedit.msc":
             keyboard.press(char)
             keyboard.release(char)
 

           keyboard.press_and_release('enter')



       elif "close group policy" in query or "close local group policy" in query:
            speak(" sorry, that application requires administrative access to close. you have close it manually")
       
       elif "open defragment" in query or "open disk optimizer" in query or "open disk optimiser" in query :
           speak("okay sir")
           os.startfile('dfrgui.exe')
           speak("shall i start optimization!")
           cm = takecommand().lower()
           if "ok" in cm or "start" in cm or "as you wish" in cm or "okay" in cm:
               import keyboard
               speak(" starting disk optimization for local disk c")
               keyboard.press_and_release('alt + o')
           else:
               speak("okay")

       elif "close defragment" in query or "close disk optimizer" in query:
           speak(" as you wish sir")
           os.system('TASKKILL /f /im dfrgui.exe')


       elif "save it" in query:
           import keyboard
           speak(" okay")
           keyboard.press_and_release('ctrl + s')


       elif "hit enter" in query or "press enter" in query:
           import keyboard
           keyboard.press_and_release('enter')



       elif "type" in query:
           import keyboard
           cm = query.replace("type"," ")
           for char in f"{cm}":
               keyboard.press_and_release(char)

       elif "show" in query:
           import keyboard
           cm = query.replace("show"," ")
           for char in f"{cm}":
               keyboard.press_and_release(char)
           keyboard.press_and_release('enter')

       elif "open amazon" in query:
           speak(" opening amazon")
           webbrowser.open("www.amazon.com")


       elif "delete it" in query or "delete folder" in query:
           import keyboard
           keyboard.press_and_release('delete')
           speak("done")

       elif "open advance menu" in query or "open advanced menu" in query or "Advanced menu" in query:
           import keyboard
           keyboard.press_and_release('windows + a')

       elif "close advance menu" in query or "close advanced menu" in query:
           import keyboard
           keyboard.press_and_release('windows + a')

       elif "open start" in query:
           import keyboard
           keyboard.press_and_release('windows')

       elif "close start" in query:
           import keyboard
           keyboard.press_and_release('windows')

       elif "select" in query:
           import keyboard
           cm = query.replace("select"," ")
           for char in f"{cm}":
               keyboard.press_and_release(char)
                   
           speak("done")


       elif "delete" in query:
           import keyboard
           cm = query.replace("delete"," ")
           for char in f"{cm}":
               keyboard.press_and_release(char)

           keyboard.press_and_release('delete')

       elif "go left" in query:
           import keyboard
           keyboard.press_and_release('left arrow')

       elif "minimise" in query:
           import keyboard
           keyboard.press_and_release('win + m')
       elif "undo" in query or "redo" in query:
           import keyboard
           keyboard.press_and_release('win + z')


      
           


       elif "go right" in query:
           import keyboard
           keyboard.press_and_release('right arrow')

       elif "open my project" in query or "open my project folder" in query:
           path = "C:\\projects"
           speak(" as you wish")
           os.startfile(path)
           speak("sir currently you are working on my upgrade. shall i explain your project?")
           query = takecommand().lower()
           if "yes" in query or "yeah" in query or "explain" in query:
               speak("sir. crystal.py represents my actual program which is built on python. you can access me on clicking crystal.bat file on the desktop. I will stay on backgroung until you tell me to go offline. or you can access me directly on python. to see my backend process like how iam peforming tasks. The test underscore represents different trial peformed by you in order to make me peform different task. for example test_internet.py is used to check whether the internet is active or not. Like this many other task are peformed")
           elif "no" in query:
               speak("as you wish")

       else:
           ans=Reply(query)
           
           file=open('C:\\ai\\ai.txt','w')
           file.write(ans)
           file.close()
           path = "C:\\ai\\ai.txt"
           
           os.startfile(path)
             
           speak(ans)

       
           
       
         
           
     



       

           
           







def quite():
    import sys
    sys.exit()





          
      # print("anything else?")     
if __name__ == "__main__":
    
    check()
    wake()
    wish()
    
