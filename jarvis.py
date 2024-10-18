import os
import speech_recognition as sr
from google.cloud import speech
from google.cloud import texttospeech

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_google_credentials.json"

# Function to recognize speech using Google's Speech-to-Text API
def recognize_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speech_client = speech.SpeechClient()
        audio_content = audio.get_wav_data()
        audio = speech.RecognitionAudio(content=audio_content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        response = speech_client.recognize(config=config, audio=audio)
        for result in response.results:
            return result.alternatives[0].transcript

    except Exception as e:
        print(f"Error recognizing speech: {str(e)}")
        return None

# Function to convert text to speech using Google's Text-to-Speech API
def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, 
        voice=voice, 
        audio_config=audio_config
    )

    # Save the audio file
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("Audio content written to 'output.mp3'")

    # Play the speech
    os.system("mpg321 output.mp3")  # For Linux (use appropriate player for your OS)

# Main assistant function
def jarvis_assistant():
    print("Welcome to Jarvis, your voice assistant!")
    
    while True:
        # Recognize speech input
        command = recognize_speech()
        if command:
            print(f"You said: {command}")

            # Simple command processing logic
            if "hello" in command.lower():
                response = "Hello! How can I assist you today?"
            elif "how are you" in command.lower():
                response = "I'm Jarvis, your AI assistant, and I'm here to help you!"
            elif "exit" in command.lower() or "bye" in command.lower():
                response = "Goodbye! Have a great day!"
                text_to_speech(response)
                break
            else:
                response = "I'm sorry, I didn't understand that."

            # Convert the response text to speech
            text_to_speech(response)
        else:
            print("No command recognized.")

# Run the assistant
if __name__ == "__main__":
    jarvis_assistant()
