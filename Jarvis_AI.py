import datetime
import random
import smtplib
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir !!")
    else:
        speak("Good Evening sir!!")

    speak("I am Jarvis,how may i help you")

def Takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f'The user said: {query}\n')

    except Exception as e:
        #print(e)
        print("Say that again please!!")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ksbalaji976@gmail.com','KSD@ivya321')
    server.sendmail('ksbalaji976@gmail.com',to,content)
    server.close()

    speak('Email sent')





if __name__=="__main__":
   WishMe()
   while True:
       query=Takecommand().lower()
       if 'wikipedia' in query:
           speak("Searching wikipedia......")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=1)
           speak("According to wikipedia")
           print(results)
           speak(results)


       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'play music' in query:
           music_dir='C:\\Users\\Balaji\\Downloads\\music'
           songs=os.listdir(music_dir)
           x=random.randint(1,13)
           os.startfile(os.path.join(music_dir,songs[x]))

       elif 'tell me the current time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f'The time is: {strTime}')
           print(strTime)

       elif 'open pycharm' in query:
           codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
           os.startfile(codepath)

       elif 'send email to balaji' in query:
           try:
               speak('What should i say sir?')
               content=Takecommand()
               to='ksbalaji976@gmail.com'
               sendEmail(to,content)

           except Exception as e:
               print(e)
               speak("Sorry email was not able to send!")

       elif 'sleep' in query:
           quit()
