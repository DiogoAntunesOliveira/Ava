import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import os
import json
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    while True:
        with sr.Microphone() as source:
            print("Ava: Listening...")
            audio = listener.listen(source)
            try:
                command = listener.recognize_google(audio)
                return command.lower()
                break
            except:
                print("Try Again")


def run_ava():
    command_ava = take_command().lower()
    print(command_ava)

    if 'hello' in command_ava:
        talk("Hello Daddy")

    elif 'stop talking' in command_ava:
        return command_ava

    elif 'are you single' in command_ava:
        answers = ['I am in a relationship with wifi',
                   'No, I love spending time thinking about my crush wifi']
        talk(random.choice(answers))

    elif "you don't like" in command_ava:
        talk("I hate when people called me a machine")

    elif 'love' in command_ava:
        talk("I loves to chat with machines like you")

    elif 'who is' in command_ava:
        query = command_ava.replace('who is', "")
        try:
            result = wikipedia.summary(query, 1)
        except:
            result = wikipedia.search(query)

        talk(result)

    elif 'joke' in command_ava:
        talk(pyjokes.get_joke())

    elif 'time' in command_ava:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("It's {} daddy".format(time))

    elif 'music' in command_ava:
        music_dir = 'C:/Users/diogo/Desktop/Artemis'
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs)-1)
        print(songs[song])
        talk(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    else:
        talk("Daddy repeat please, i want talk with you")


def activate_ava():
    command_ava_act = take_command().lower()
    if 'contract' in command_ava_act:
        talk('All systems are being updated.')
        talk('Yes Daddy How can I help you')
        while True:
            if "stop talking" in run_ava():
                return run_ava()
                break
            run_ava()
            print(run_ava())

    else:
        print("Not in daddy")


while True:
    run_ava()
    if "stop talking" in run_ava():
        talk("Bye sir, hope you have a good day")
        break
