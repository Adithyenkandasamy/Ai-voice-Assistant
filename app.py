import google.generativeai as genai
from gtts import gTTS
import os
import speech_recognition as sr
from playsound import playsound  # Import playsound to play audio files
import take_command as tc  # Module for taking voice commands
import date_time as dt  
import webbrowser as wb


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

def speak_in_tanglish(text):
    # Convert the text to speech in Tanglish
    tts = gTTS(text=text, lang='ta')  # Use Tamil language for pronunciation
    tts_file = 'response.mp3'
    tts.save(tts_file)  # Overwrite the existing MP3 file with the new response
    playsound(tts_file)  # Play the updated audio file
    return tts_file

def listen_to_command():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and listen for a command
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Use Google Web Speech API to recognize the audio
        command = recognizer.recognize_google(audio, language='ta-IN')  # Set language to Tamil
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    model = configure_ai()
        
    while True:
        ai_prompt = listen_to_command()  # Listen for a command in Tanglish
        if ai_prompt:
            ai_response = generate_ai_response(model, ai_prompt)
            print("AI Response:", ai_response)  # Optional: Print the response to console
            speak_in_tanglish(ai_response)  # Speak the AI response

if __name__ == "__main__":
    main()
