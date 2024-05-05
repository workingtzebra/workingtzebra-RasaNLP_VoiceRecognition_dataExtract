import subprocess
import json
import speech_recognition as sr
from datetime import datetime
import pandas as pd
import time
# Initialize the recognizer
r = sr.Recognizer()

def transcribe_audio(audio_path):
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        try:
            # Using Google Web Speech API to transcribe
            return r.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def run_rasa_nlu(message):
    # Construct the command to run Rasa shell
    command = f'echo "{message}" | rasa shell nlu'
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    try:
        # Extract JSON output
        start_index = result.stdout.index('Next message:') + len('Next message:')
        end_index = result.stdout.index('Next message:', start_index)
        json_string = result.stdout[start_index:end_index].strip()
        json_output = json.loads(json_string)
        
        # Extracting relevant information
        entities = json_output.get('entities', [])
        extracted_data = {}
        for entity in entities:
            if entity['entity'] in ['source', 'destinition', 'date', 'time']:
                extracted_data[entity['entity']] = entity['value']

        # Set default date and time if not present
        extracted_data.setdefault('date', datetime.now().strftime('%Y-%m-%d'))
        extracted_data.setdefault('time', datetime.now().strftime('%H:%M:%S'))
        
        return extracted_data

    except ValueError:
        print("JSON start or end tag not found in output.")
        return None
    except json.JSONDecodeError:
        print("Failed to decode JSON from output.")
        return None

def save_to_csv(data):
    print("Loading CSV file...")
    file_name = 'travel_data.csv'
    df = pd.DataFrame([data])
    
    # Check if the CSV file exists and append if it does; else write a new file
    try:
        with open(file_name, 'a') as f:
            df.to_csv(f, index=False, header=f.tell() == 0)
            print("Data saved in CSV successfully!")
    except FileNotFoundError:
        df.to_csv(file_name, index=False)

# Accepting file name input from the user
file_base_name = input("Enter the base file name (without extension): ")
audio_file_path = f"{file_base_name}.wav"
print("Processing audio...")
time.sleep(2)
print("Generating response...")
text_string = transcribe_audio(audio_file_path)
print("Transcripted Text: ", text_string)
print("Sending Data to NLP Engine...")
print("Processing.....")
data = run_rasa_nlu(text_string)

if data:
    save_to_csv(data)
