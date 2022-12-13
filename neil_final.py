import pyttsx3  #pip install pyttsx3,speechRecognition,pyAudio,wikipedia,AppOpener
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from AppOpener import run
engine = pyttsx3.init('sapi5') #used for voices
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello,my name is neil, how may I help you?")

def takeCommand():
    #takes microphone input from user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User-said: {query}\n")
    except Exception as e:
        print("Tell something valid")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'weather' in query:
            webbrowser.open("accuweather.com")
        elif 'spotify' in query:
            run("spotify")
        elif 'play music' in query:
            run("spotify")
        elif 'exit' in query:
            speak("Thank you for using neil")
            exit()
        
         
        elif 'take photo' in query:
            run("camera")
        