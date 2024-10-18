import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voice=engine.getProperty('voices')
    rate=engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()

    

