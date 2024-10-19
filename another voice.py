import os
from google.cloud import texttospeech
from playsound import playsound

# Set the path to your Google Cloud service account JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your-service-account-file.json"

# Function to convert text to speech
def google_tts(text, language_code='en-US', gender='neutral', speaking_rate=1.0):
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language and the gender
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender[gender.upper()]
    )

    # Select the audio format (MP3)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice_params,
        audio_config=audio_config
    )

    # Save the audio file
    audio_file = 'output.mp3'
    with open(audio_file, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{audio_file}"')

    # Play the audio
    play_audio(audio_file)

# Function to play the audio file
def play_audio(file_path):
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Main function to get user input and process it
def main():
    text = input("Enter the text you want to convert to speech: ")
    language_code = input("Enter the language code (e.g., en-US, fr-FR, ta-IN): ")
    gender = input("Enter the voice gender (male, female, neutral): ").lower()
    speaking_rate = float(input("Enter the speaking rate (default is 1.0): ") or "1.0")

    # Call the google_tts function
    google_tts(text, language_code, gender, speaking_rate)

if __name__ == "__main__":
    main()
