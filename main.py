import google.generativeai as genai
import pathlib
import time
import pyttsx3
import os
import webbrowser as wb
import pyautogui
import pyjokes
import take_command as tc  # Module for taking voice commands
import respond as rs  # Module for text-to-speech responses
import date_time as dt  # Module for greeting based on time

# Assistant and User Info
assis_name = "Jarvis"
boss_name = "Gokul"

# Configure the Google AI model
def configure_ai():
    genai.configure(api_key="AIzaSyBb9ONZYSIImDtFhlXccVk0pgAvlIDoc7A")
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

# Generate response using the AI model
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

# Tell jokes using pyjokes
def tell_jokes():
    return pyjokes.get_joke()

# Respond to various commands
def respond(text, model):
    if "hello" in text:
        rs.say(dt.wishing())
        rs.say("How can I help you?")
    elif "what is your name" in text:
        rs.say(f"My name is {assis_name}")
    elif "tell my name" in text:
        rs.say(f"Your name is {boss_name}")
    elif "how are you" in text:
        rs.say("I am fine")
    elif "tell me a joke" in text:
        rs.say(tell_jokes())
    elif "mode" in text:

        rs.say("Entering AI mode. How can I assist?")
        ai_prompt = tc.takecommand()
        ai_response = generate_ai_response(model, ai_prompt)
        rs.say("I am analyzing")
        rs.say(ai_response)
    elif "instagram" in text:
        rs.say("Opening Instagram")
        wb.open("https://www.instagram.com")
    elif "github" in text:
        rs.say("Opening GitHub")
        wb.open("https://www.github.com")
    elif "search" in text:
        rs.say("Where do you want to search?")
        search_platform = tc.takecommand().lower()
        if "youtube" in search_platform:
            rs.say("What do you want to search on YouTube?")
            search_query = tc.takecommand()
            rs.say(f"Searching for {search_query} on YouTube.")
            wb.open(f"https://www.youtube.com/results?search_query={search_query}")
            control_youtube()
        elif "google" in search_platform:
            rs.say("What do you want to search on Google?")
            search_query = tc.takecommand()
            rs.say(f"Searching for {search_query} on Google.")
            wb.open(f"https://www.google.com/search?q={search_query}")
    elif "shutdown the computer" in text:
        rs.say("Shutting down the computer.")
        os.system('shutdown now')
    elif "restart the computer" in text:
        rs.say("Restarting the computer.")
        os.system('reboot')
    elif "open terminal" in text:
        rs.say("Opening Terminal.")
        os.system('gnome-terminal')
    elif "Bye" in text:
        rs.say("Goodbye, have a great day!")
        exit()

# Control YouTube playback using pyautogui
def control_youtube():
    rs.say("Do you want to control the video? Say a command like play, pause, mute, or stop.")
    while True:
        control_command = tc.takecommand().lower()
        if "play the video" in control_command or "pause the video" in control_command:
            rs.say("Toggling play/pause on the video.")
            pyautogui.press('space')
        elif "mute the video" in control_command:
            rs.say("Muting the video.")
            pyautogui.press('m')
        elif "unmute the video" in control_command:
            rs.say("Unmuting the video.")
            pyautogui.press('m')
        elif "full screen" in control_command:
            rs.say("Toggling full screen.")
            pyautogui.press('f')
        elif "volume up" in control_command:
            rs.say("Increasing volume.")
            pyautogui.press('up')
        elif "volume down" in control_command:
            rs.say("Decreasing volume.")
            pyautogui.press('down')
        elif "stop" in control_command or "exit" in control_command:
            rs.say("Exiting YouTube control mode.")
            break
        else:
            rs.say("Sorry, I didn't understand that command.")

# Main function to initialize the assistant
def main():
    model = configure_ai()  # Initialize the AI model
    
    rs.say("hi my name is jarvis i am ur ai assistant,ok tell how can i help u ?")
    while True:
        # Listen for a voice command
        text = tc.takecommand().lower()
        print(f"You said: {text}")
        
        # Process the command
        respond(text, model)

if __name__ == "__main__":
    main()
