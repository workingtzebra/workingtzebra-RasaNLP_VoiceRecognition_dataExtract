
# Project Overview
This project utilizes Rasa for natural language understanding and speech recognition to extract data from spoken commands.

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
rasa train
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
