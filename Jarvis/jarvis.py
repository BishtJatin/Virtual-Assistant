from email.mime import audio
from http import server
from importlib.resources import contents
import string
from unittest import result
from urllib.parse import _ResultMixinStr
import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import pyjokes


 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir.Speed 1 terahertz, memory 1 zeta byte. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif'open github' in query:
            webbrowser.open("github.com")

        elif'play music' in query:
            music_dir = 'C:\\Users\\jatin\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif'open code' in query:
            codePath = "C:\\Users\\jatin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif'date' in query:
            speak('sorry, Sir i know the story of dilip')
        
        elif'single' in query:
            speak('sorry, Sir dilip ki story sunn k mera mann nhi karta')
        
        elif'friends' in query:
            speak('sorry, Sir i donot have friends')
        
        elif'maker' in query:
            speak('jatin sir,')
            
        elif'quotes' in query:
            speak('Wake up to reality! Nothing ever goes as planned in this world. The longer you live, the more you realize that in this reality, only pain, suffering, and futility exist.')
            
        elif'gussa' in query:
            speak('Bahut taklif hoti hai jab aap yogya ho aur log aapki yogyta na pahchane.')
            
        elif'raja' in query:
            speak('Yeh Hai hamara Palace… yahan main hoon raja or tum ho rani.')


        elif'jhooth' in query:
            speak('jhooth to Kewal insaan Bolta hai, Machines nahe bolte')

        elif'joke' in query:
            speak(pyjokes.get_joke())

        elif'email to jatin' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jatinbisht1902@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend jatin bhai. I am not able to send this email")


        