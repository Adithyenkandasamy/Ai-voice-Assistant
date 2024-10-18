import pyttsx3
import os
import webbrowser as wb
import pyautogui
import respond as rs
import take_command as tc
import pyjokes
import date_time as dt
import main as m  # Import the MyAIModel class and any other necessary items
import google.generativeai as genai

assis_name = "Jarvis"
boss_name = "Adhii"

# AI Model class that integrates with the Gemini API
class MyAIModel:
    def __init__(self):
        # Configure API key for Gemini API
        genai.configure(api_key="YOUR_GEMINI_API_KEY")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def test_text_gen_text_only_prompt(self, prompt):
        # Generate response from Gemini AI based on user input
        response = self.model.generate_content(prompt)
        return response

# Instance of AI Model
my_model = MyAIModel()

# Function to tell jokes
def tell_jokes():
    joke = pyjokes.get_joke()
    return joke

# Respond function to handle user input
def respond(text):
    if "hello" in text:
        rs.say(dt.wishing())
        rs.say("How can I help you?")
    elif "activate" in text:
        rs.say("Activating voice assistant")
        while True:
            rs.say("I'm listening. Please give a prompt.")
            my_idea = tc.takecommand().lower()  # Get voice input from the user
            if my_idea:  # Check if there is any input
                content = my_model.test_text_gen_text_only_prompt(my_idea)  # Get AI-generated content
                rs.say(content)  # Speak out the generated content

            # Option to break the loop after a command
            if "exit" in my_idea or "stop" in my_idea:
                rs.say("Exiting voice assistant mode.")
                break
    elif "tell me a joke" in text:
        rs.say(tell_jokes())
    elif "Bye" in text or "bhai" in text:
        rs.say("Bye sir, have a good day.")
        exit()

# Main loop for voice assistant
while True:
    rs.say("Say something, sir")
    text = tc.takecommand()  # Wait for a command from the user
    print(text)
    respond(text)  # Respond based on the input
