import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

while True:
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
                command=command.replace("alexa ","")
                (command)
        return command

    def shefy_command():
        command=alexa_command()
        print("YOU> ",command)
        shefy={
            "hai":"hello",
            "hay":"hello",
            "hi":"hello",
            "hello":"hello",
            "how are you":"i am fine thankyou!",
            "what is your name":"my name is alexa",
            "what is your age":"i am a computer",
            "where do you live":"i live in jabalpur",
            "who are you":"i am a computer",
            "hu r u":"i am a computer",
        }
        if command in shefy:
            b=(shefy[command])
            print("ALEXA> " + b)
            talk(b)
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
            
    shefy_command()
