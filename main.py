from google.cloud import texttospeech
from google.oauth2 import service_account
from dotenv import load_dotenv
import os
import argparse


# Load environment variables from .env file
load_dotenv()


# Get the path to the service account JSON from the .env file
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def text_to_speech(text, output_file):
    output_file_name = output_file if output_file.endswith(".mp3") else output_file + ".mp3"

    # If one were to productionize, you'd want to do this to hide your serivce account.
    # credentials = service_account.Credentials.from_service_account_file("/path/to/service_account.json")
    # client = texttospeech.TextToSpeechClient(credentials=credentials)

    client = texttospeech.TextToSpeechClient()


    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open(output_file_name, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {output_file_name}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert text to speech')
    parser.add_argument('text', help='The text you want to convert')
    parser.add_argument('output', help='The name of the output file')
    # Parse arguments
    args = parser.parse_args()
    
    # Call conversion function
    text_to_speech(args.text, args.output)


if __name__ == '__main__':
    main()
