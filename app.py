import google.generativeai as genai
from gtts import gTTS
import os
import webbrowser as wb
import pyautogui
import pyttsx3
import pyjokes
import speech_recognition as sr
import take_command as tc  # Module for taking voice commands
import respond as rs  # Module for speaking responses
import date_time as dt  # Module for date/time responses
from playsound import playsound

assis_name = "Jarvis"
boss_name = "Gokul"

def configure_ai():
    genai.configure(api_key="AIzaSyBb9ONZYSIImDtFhlXccVk0pgAvlIDoc7A")
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

def generate_ai_response(model, prompt):
    try:
        response = model.generate_content(prompt)
        if response and response.candidates:
            generated_text = response.candidates[0].content.parts[0].text
            return generated_text
        else:
            return "Sorry, I didn't understand that."
    except Exception as e:
        return f"Error generating AI response: {str(e)}"

def tell_jokes():
    return pyjokes.get_joke()

def speak_in_tanglish(text):
    tts = gTTS(text=text, lang='ta')
    tts_file = 'response.mp3'
    tts.save(tts_file)
    playsound(tts_file)

def execute_command(text):
    if "hello" in text:
        rs.say(dt.wishing())
        rs.say("How can I help you?")
    elif "your name" in text:
        rs.say(f"My name is {assis_name}")
    elif "my name" in text:
        rs.say(f"Your name is {boss_name}")
    elif "how are you" in text:
        rs.say("I am fine.")
    elif "tell a joke" in text:
        rs.say(tell_jokes())
    elif "open calculator" in text:
        rs.say("Opening the calculator")
        os.system('gnome-calculator')
    elif "search" in text:
        rs.say("Where do you want to search?")
        What_search = tc.takecommand().lower()
        if "youtube" in What_search:
            rs.say("Sorry, enala itha seiya mudiyathu.")  # Custom response for blocking YouTube search
        elif "google" in What_search:
            rs.say("What do you want to search on Google?")
            search_query = tc.takecommand()
            rs.say(f"Searching for {search_query} on Google.")
            wb.open(f"https://www.google.com/search?q={search_query}")
    elif "shutdown" in text:
        rs.say("Shutting down the computer.")
        os.system('shutdown now')
    elif "restart" in text:
        rs.say("Restarting the computer.")
        os.system('reboot')
    elif "lock" in text:
        rs.say("Locking the computer.")
        os.system('gnome-screensaver-command -l')
    elif "open firefox" in text:
        rs.say("Opening Firefox.")
        os.system('firefox')
    elif "open terminal" in text:
        rs.say("Opening Terminal.")
        os.system('gnome-terminal')
    elif "Bye" in text or "bye" in text:
        rs.say("Goodbye! Have a great day!")
        exit()

def control_video():
    rs.say("You can control the video. Say commands like play, pause, mute, or stop.")
    while True:
        command = tc.takecommand().lower()
        if "play" in command or "pause" in command:
            pyautogui.press('space')
        elif "mute" in command:
            pyautogui.press('m')
        elif "unmute" in command:
            pyautogui.press('m')
        elif "volume up" in command:
            pyautogui.press('up')
        elif "volume down" in command:
            pyautogui.press('down')
        elif "stop" in command or "exit" in command:
            rs.say("Exiting control mode.")
            break
        else:
            rs.say("Sorry, I didn't understand that command.")

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language='ta-IN')
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Error: {str(e)}"

def main():
    model = configure_ai()

    while True:
        ai_prompt = listen_to_command()  # Listen to Tanglish command
        if ai_prompt:
            ai_response = generate_ai_response(model, ai_prompt)
            print(f"AI Response: {ai_response}")
            speak_in_tanglish(ai_response)  # Speak the AI response
            execute_command(ai_response.lower())  # Process command from AI response

if __name__ == "__main__":
    main()
