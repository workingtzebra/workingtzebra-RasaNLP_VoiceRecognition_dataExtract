
# Project Overview
This project utilizes Rasa for natural language understanding and speech recognition to extract data from spoken commands.

**[NOTE] Only Python version above 3.4 and below or equal to 3.8 is supported currently. Make sure to select the correct interpreter.**

## Installation and Setup
1. **Install Rasa**:
   ```bash
   pip install rasa
   ```

2. **Configure Rasa**:
   - `config.yml`: Defines the recipe and language model configuration.
   - `domain.yml`: Specifies the intents, entities, responses, and actions available to the Rasa assistant.
   - `credentials.yml`: Contains credentials needed for integrating with various messaging channels.

## Training the Model
Use the training data in the `data/` directory to train the model:
- `nlu.yml`: Training examples for intent recognition and entity extraction.
- `stories.yml`: Training stories to help Rasa understand conversation flows.
- `rules.yml`: Rules defining specific actions triggered by intents.

To train the model, run:
```bash
rasa train nlu
```

## Running the Application
After training the model, start the Rasa server and action server:
```bash
rasa run actions
rasa shell
```
In `jsonF.py`, enter a base file name for the audio file to process. The script will transcribe the speech, send the text to Rasa NLU, and save the extracted data to `travel_data.csv`.

## Additional Files
- `actions.py`: Custom actions executed by Rasa in response to user inputs.
- `endpoints.yml`: Configures endpoints for model storage, custom actions, and event brokers.

## Running `jsonF.py`
The `jsonF.py` script is the main entry point of the application:
1. Ensure the Rasa server and action server are running as mentioned previously.
2. Run the script:
   ```bash
   python jsonF.py
   ```
3. You will be prompted to enter the base file name of an audio file (without extension). The script expects a `.wav` file with the given name to exist in the same directory.
4. The script processes the audio file to transcribe the speech to text, sends this text to Rasa NLU, and saves the extracted data into a CSV file named `travel_data.csv`.
