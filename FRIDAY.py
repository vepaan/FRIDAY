from __future__ import print_function, unicode_literals
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import json
from facepplib import FacePP, exceptions
import cv2,time
import numpy as np
import json
import requests
import sys
import playsound

posrespond = 'Glad to know Boss','Wow great boss','Sounds amazing','Same here','Of course you will have a good day Boss','Wow'
negrespond = 'dont worry Boss things like this happen','Maybe you could do with some music','Perhaps you should find ways to keep your spirits up','Lift your mood up','Entertain yourself boss','Now I am also not feeling too good Boss'

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir said: {query}\n")

    except Exception as e:    
        print("Say that again please...")
        speak("Sir I am having difficulty in hearing you")
        return "None"
        return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate' , 195)

while True:
    print('Stand by for retinal and biometrics scan')
    speak('Stand by for retinal and biometrics scan')
    img=cv2.VideoCapture(0)
    check, frame = img.read()
    cv2.imwrite('C:/IMP/Music/test.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
    cv2.waitKey()
    img.release()
    face_detection=""
    faceset_initialize=""
    face_search=""
    face_landmarks=""
    dense_facial_landmarks=""
    face_attributes=""
    beauty_score_and_emotion_recognition=""
    def face_comparing(app):
        img_file1="C:/IMP/Music/20200525_182200.jpg"
        img_file2="C:/IMP/Music/test.jpg"
        cmp_ = app.compare.get(image_file1=img_file1,image_file2=img_file2)
        print('Matching percent', '=', cmp_.confidence)
        if cmp_.confidence>70:
            print("Retinal and biometrics scan accepted")
            speak('Retinal and Biometrics scan accepted')
            for passwordcount in range(1,4):
                while True:
                    passwordcount=passwordcount+1
                    speak("Enter the password for authorization")
                    pw=input("Enter the password for authorization: ")
                    if pw=="pointbreak":
                        print("ACCESS GRANTED!")
                        speak("ACCESS GRANTED")
                        print("  0     0 000000 0      000000 000000 00   00 000000     000000 000000 000000 ") 
                        print("  0     0 0      0      0      0    0 0 0 0 0 0          0        0    0    0 ")      
                        print("  0  0  0 000000 0      0      0    0 0  0  0 000000     000000   0    000000 ")
                        print("  0 0 0 0 0      0      0      0    0 0     0 0               0   0    0 00   ")      
                        print("  00   00 000000 000000 000000 000000 0     0 000000     000000 000000 0   00 ")
                        def wishMe():
                            hour = int(datetime.datetime.now().hour)
                            if hour>=0 and hour<12:
                                speak("Good Morning Boss.")
                                print("Good Morning Boss.")

                            elif hour>=12 and hour<18:
                                speak("Good Afternoon Boss.")   
                                print("Good Afternoon Boss.")

                            else:
                                speak("Good Evening Boss.")
                                print("Good Evening Boss")

                            speak("Please tell me how may I help you")
                            print("Please tell me how may I help you")

                        def takeCommand():

                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("Listening...")
                                r.pause_threshold = 0.5
                                audio = r.listen(source)

                            try:
                                print("Processing...")    
                                query = r.recognize_google(audio, language='en-in')
                                print(f"Sir said: {query}\n")

                            except Exception as e:    
                                print("Sir I am having difficulty in hearing you...")
                                speak("Sir I am having difficulty in hearing you")
                                return "None"
                            return query

                        def sendEmail(to, content):
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls()
                            server.login('rockstarktm7@gmail.com', 'password')
                            server.sendmail('binapanta13@yahoo.com', to, content)
                            server.close()

                        if __name__ == "__main__":
                            wishMe()
                            while True:
                                query = takeCommand().lower()
                                if 'wikipedia' in query:
                                    query = query.replace("wikipedia", "")
                                    if query=="":
                                        speak('Boss could you specify what to search')
                                        print('Boss could you specify what to search')
                                    else:
                                        speak('Searching Wikipedia...')
                                        results = wikipedia.summary(query, sentences=2)
                                        speak("According to Wikipedia")
                                        print(results)
                                        speak(results)

                                elif 'open youtube' in query:
                                    webbrowser.open("youtube.com")

                                elif 'word' in query:
                                    wordPath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010'
                                    os.startfile(wordPath)

                                elif 'powerpoint' in query:
                                    powerpointPath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Powerpoint 2010'
                                    os.startfile(powerpointPath)

                                elif 'outlook' in query:
                                    outlookPath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Outlook 2013.lnk'
                                    os.startfile(outlookPath)

                                elif 'idiot' in query:
                                    speak('Sorry sir i am working on it')

                                elif 'open google' in query:
                                    webbrowser.open("google.com")
                                elif 'open facebook' in query:
                                    webbrowser.open("facebook.com")

                                elif 'speed' in query:
                                    speak('Do you want my talking to be fast or slow sir')
                                    if 'slow' in query:
                                        engine.setProperty('rate', 190)
                                        speak('What do you think about this sir')
                                        if 'good' in query:
                                            break
                                        if 'bad' in query:
                                            engine.setProperty('rate', 180)
                                            speak('Sir I hope you are fine with this because my speed going less clearly means your time being wasted')
                                            break
                                    elif 'fast' in query:
                                        engine.setProperty('rate', 210)
                                        speak('What about this')
                                        if 'good' in query:
                                            break
                                        if 'bad' in query:
                                            engine.setProperty('rate', 220)
                                            speak('Sir I am extremely sorry but if I go beyond this i will not be audible')
                                            break
                                                
                                elif 'volume' in query:
                                    speak('What would you like my volume of talking to be sir')
                                    v=int(input("Please enter the volume: "))
                                    engine.setProperty('volume', v)

                                elif 'kill' in query:
                                    sys.exit()

                                elif 'footage' in query:
                                    cameraPath = "C:\IMP\STARK INDUSTRIES_74\ALL FILES\chat.py"
                                    os.startfile(cameraPath)
                                    
                                elif 'laws' in query:
                                    print('1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.')
                                    print('2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.')
                                    print('3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.')
                                    speak('A robot may not injure a human being or through inaction allow a human being to come to harm')
                                    speak('A robot must obey the orders given it by human beings except where such orders would conflict with the First Law')
                                    speak('A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws')

                                
                                elif 'open amazon' in query:
                                    webbrowser.open("amazon.com")

                                elif 'teams' in query or 'study time' in query or 'online class' in query:
                                    webbrowser.open('https://teams.microsoft.com/_?culture=en-us&country=WW&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/Mathematics?threadId=19:ea88bfb7d6de4b8e952a95cfd8681f8d@thread.tacv2&ctx=channel')

                                elif 'chrome' in query:
                                    chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                                    os.startfile(chromePath)

                                elif 'stackoverflow' in query:
                                    webbrowser.open("stackoverflow.com")

                                elif 'weather' in query:
                                    api_key = 'xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
                                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                                    city_name = 'Kathmandu'
                                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                                    response = requests.get(complete_url)
                                    x = response.json()
                                    print(x)
                          
                                elif 'open hacker' in query:
                                    webbrowser.open("geektyper.com")

                                elif 'who are you' in query:
                                    speak('I am Friday sir, and I stand for Female Replacement Intelligent Digital Assistant Youth ') 
                                    print("I am F.R.I.D.A.Y sir, and I stand for Female Replacement Intelligent Digital Assistant Youth ")

                                elif 'what do you stand for' in query or 'what is your full form' in query:
                                    speak('I am Friday sir, and I stand for Female Replacement Intelligent Digital Assistant Youth ') 
                                    print("I am F.R.I.D.A.Y sir, and I stand for Female Replacement Intelligent Digital Assistant Youth ")

                                elif 'who made you' in query:
                                    speak('Well i was created by you but to be exact i was created by mr vision.')

                                elif 'friday' in query:
                                    r = sr.Recognizer()
                                    query = query.replace("friday", "")
                                    if query=="":
                                         list1='Yes boss','Always here boss','Right here how may i assist you boss','At your service boss'
                                         speak(random.choices(list1,k=1))
                                    else:
                                         r = sr.Recognizer()
                                         with sr.Microphone() as source:
                                             r.pause_threshold = 1
                                             audio = r.listen(source)

                                elif 'translator' in query:
                                    webbrowser.open('G://STARK INDUSTRIES_74//translator.py')
                                    
                                    
                                elif 'stark industries database' in query:
                                    speak('will do')
                                    webbrowser.open('G://STARK INDUSTRIES_74')

                                elif 'how are you' in query or 'how are you doing' in query:
                                    response = 'I am Ok you boss', "I'm fine what about you Boss", 'I had a rough day but I am fine how was your day boss', 'good what about you Boss', 'I had a wonderful time Thanks for asking Boss what about you'
                                    speak(random.choices(response, k=1))
                 
                                    
                                    if 'good' in query or 'great' in query or 'doing well' in query:
                                        speak(random.choices(posrespond, k=1))

                                    elif 'bad' in query or 'not very good' in query or 'not good' in query:
                                        speak(random.choices(negrespond, k=1))
                                        
                                elif 'pronouncer' in query:
                                    speak('What would you like me to pronounce sir')
                                    while True:
                                        a=str(input("Word to be pronounced: "))
                                        if a=='stark_stop':
                                            break
                                        else:
                                            speak(a)

                                elif 'open security system' in query:
                                    speak('Voice activation required')
                                    print("Voice activation required")


                                elif 'open section 17' in query:
                                    speak('requesting confirmation sir you said open the barrier')

                                elif 'deploy mark 50' in query:
                                    speak('sir the mark 50 is not ready for deployment')
                                
                                elif 'do it' in query:
                                    speak('as your wish sir done')

                                elif 'bored' in query:
                                    speak('Well in that case you must find ways to entertain yourself boss')

                                elif 'music' in query:
                                    playsound.playsound('G:\\Music\\ACDC - Back In Black (Official Video).mp3',True)  
                                                
                                elif 'time' in query:
                                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                                    speak(f"Sir, the time is {strTime}")
                                    print(f"Sir,the time is {strTime}")

                                elif 'open code' in query:
                                    codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                                    os.startfile(codePath)

                                elif 'email' in query:
                                    try:
                                        speak("What should I say?")
                                        content = takeCommand()
                                        to = "binapanta13@yahoo.com"    
                                        sendEmail(to, content)
                                        speak("Email has been sent!")
                                    except Exception as e:
                                        print(e)
                                        speak("Sorry boss. I am not able to send this email")

                                elif 'search' in query or 'check' in query:
                                    speak('Whom would you like me to search boss')
                                    speak('     and boss could you type it in lowercase')
                                    j=str(input('Whom would you like me to search boss: '))
                                    speak('Here are the search results in my database boss')
                                    if j=='<name hidden for privacy>':
                                        print('Name: name')
                                        print('Job: Student')
                                        print('Address: Kathmanu, Nepal')
                                        print('Current status is active and is not a threat to you boss.')
                                        speak('Current status is active and is not a threat to you boss.')
                                    elif j=='<name hidden for privacy>':
                                        print('Name: name')
                                        print('Job: Student')
                                        print('Address: Kathmanu, Nepal')
                                        print('Current status is active and is not a threat to you boss.')
                                        speak('Current status is active and is not a threat to you boss.')
                                        print('Claims to be the CEO of Wolf Of The Wall Street')
                                        speak('Claims to be the the CEO of wolf of the wall street')
    
                                    
                                elif 'open calculator' in query:
                                    speak('Sir you are aware of the fact that I can accomplish a lot more than just calculating')
                                    if 'o' in query:
                                            speak('But since you are my creator i will do as you say sir')
                                            add = lambda x,y:x+y
                                            def add(x, y):
                                                return x + y
                                            def subtract(x, y):
                                                return x - y
                                            def multiply(x, y):
                                                return x * y
                                            def divide(x, y):
                                                return x / y
                                            def power(x ,y):
                                                return x**y
                                            print("Select operation.")
                                            speak('Select operation')   
                                            print("1.Add")
                                            speak(' Add')
                                            print("2.Subtract")
                                            speak(' Subtract')
                                            print("3.Multiply")
                                            speak(' multiply')
                                            print("4.Divide")
                                            speak(' divide')
                                            print("5.Power")
                                            speak(' power')
                                            choice = input("Enter choice(1/2/3/4/5)")
                                            num1 = int(input("Enter first number "))
                                            num2 = int(input("Enter second number "))
                                            
                                            
                                            if choice == '1':
                                                    print(num1,"+",num2,"=", add(num1,num2))
                                                    speak(f"sir the answer is {add(num1,num2)}")
                                            elif choice == '2':
                                                    print(num1,"-",num2,"=", subtract(num1,num2))
                                                    speak(f"sir the answer is {subtract(num1,num2)}")
                                            elif choice == '3':
                                                    print(num1,"*",num2,"=", multiply(num1,num2))
                                                    speak(f"sir the answer is {multiply(num1,num2)}")
                                            elif choice == '4':
                                                    print(num1,"/",num2,"=", divide(num1,num2))
                                                    speak(f"sir the answer is {divide(num1,num2)}")
                                            elif choice == '5':
                                                    print(num1,"**",num2,"=", power(num1,num2))  
                                                    speak(f"sir the answer is {power(num1,num2)}")
                        break
                    elif passwordcount==4:
                        speak("YOU ARE NOT AUTHORIZED")
                        sys.exit()
                    else:
                        print("ACCESS DENIED")
                        speak('ACCESS DENIED')

        elif cmp_.confidence<70:
            print("YOU ARE NOT AUTHORIZED!")
            speak("YOU ARE NOT AUTHORIZED")
            res='Get outta here!','You cant fool me','You had a bad day intruder? Ill make it worse','You probably felt this strong urge to die!'
            reply=(random.choices(res, k=1))
            print(reply)
            speak(reply)
            sys.exit()

    break
if __name__ == '__main__':

    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl' 
    api_secret = 'TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

    try:
        app_ = FacePP(api_key=api_key, api_secret=api_secret)
        funcs = [
            face_detection,
            face_comparing,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition
        ]
        face_comparing(app_)

    except exceptions.BaseFacePPError as e:
        print('Error:', e)
        res='Get outta here!','You cant fool me','You had a bad day intruder? Ill make it worse','You probably felt this strong urge to die!'
        reply=(random.choices(res, k=1))
        print(reply)
        speak(reply)
       

   

