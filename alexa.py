import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
# import google
# import pyChatGPT

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    with sr.Microphone() as source:
        print("Lisnening...")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if "alexa" in command:
            command=command.replace("alexa","")
            (command)
    return command

def run_alexa():
    command=alexa_command()
    print("YOU >",command,".")
    if "play" in command:
        song=command.replace("play","")
        talk("Playing" + song)
        print("ME >Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M")
        talk("Currant time is" + time)
        print("ME >Currant time is " + time)
        print(time)

    elif "tell" in command:
        person=command.replace("superstar","")
        info=wikipedia.summary(person,5)
        print("ME >",info)
        talk(info)

    # elif "my question" in command:
    #     que=command.replace("my","")
    #     ans=google(que)
    #     print("ME >",ans)
    #     talk(ans)

    # elif "alexa" in command:
    # me=command.replace("alexa","")
        # you=pyChatGPT(command)
        # print("ME >",you)
        # talk(you)
run_alexa()