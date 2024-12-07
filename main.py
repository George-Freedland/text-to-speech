from google.cloud import texttospeech
from dotenv import load_dotenv
import os
import argparse


# Load environment variables from .env file
load_dotenv()

# Get the path to the service account JSON from the .env file
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-J",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.0,  # Normal rate; adjust between 0.25 and 4.0
        pitch=0.0,          # Neutral pitch; adjust between -20.0 and 20.0
        volume_gain_db=0.0  # Normal volume; adjust between -96.0 and 16.0
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    output_file_name = "output.mp3"
    with open(output_file_name, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {output_file_name}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert text to speech')
    parser.add_argument('text', help='The text you want to convert')
    # Parse arguments
    args = parser.parse_args()
    
    # Call conversion function
    text_to_speech(args.text)


if __name__ == '__main__':
    main()
