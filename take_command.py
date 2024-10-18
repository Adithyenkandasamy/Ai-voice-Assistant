import speech_recognition as sr

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

        try:
        
            print("Recognizing...")
            text = r.recognize_google(audio,language='en-in')
            print(f"User said: {text}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")    
            return "None"
        return text
takecommand()