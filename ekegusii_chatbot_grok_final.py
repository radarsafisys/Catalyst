import os
import csv

def initialize_chatbot_responses():
    """
    Initializes the chatbot's response dictionary by loading phrases from a CSV file.
    Each key is an Ekegusii phrase, and the value is Sheila's context-aware response.
    """
    responses = {}
    csv_path = 'ekegusii_phrases.csv'
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=['phrase', 'response'])
            next(reader)  # Skip header
            for row in reader:
                responses[row['phrase']] = row['response']
        print(f"Successfully loaded {len(responses)} phrases from {csv_path}.")
    except FileNotFoundError:
        print(f"Error: {csv_path} not found. Using essential manual fallback entries.")
        manual_entries = {
            "Eng’ombe egakwa?": "Yaya? Egakwa? Teri buya, mbobe! Korende gora eyende.",
            "Chiombe chigakwa?": "Yaya? Chigakwa? Teri buya, mbobe! Korende gora echinde.",
            "Yakwete eng’ombe?": "Yaya? Yakwete? Teri buya, mbobe! Korende gora eyende.",
            "Chiakwete chiombe?": "Yaya? Chiakwete? Teri buya, mbobe! Korende gora echinde.",
            "Okokwa mama?": "Yaya? Ogokwa? Teri buya, mbobe! Nagosabeire obe buya.",
            "Ogokwa tata?": "Yaya? Ogokwa? Teri buya, mbobe! Nagosabeire obe buya.",
            "Yakwete mama?": "Yaya? Yakwete? Teri buya, mbobe! Nagosabeire obe buya.",
            "Bwakire?": "Ee, Bwakire Buya!",
            "Saba as’Omonene!": "Nagosabeire obe buya.",
            "Mbuya gwaetire?": "Ee, naetire buya! I enjoyed my time today...",
            "Inaki yaa?": "Ee, buya! Ogoeta!",
            "Ogoeta": "Ee, ogoeta buya!",
            "Obwanchani n’Obonene": "Ee, Obonene!",
        }
        responses.update(manual_entries)
    return responses

def get_audio_filepath(phrase):
    """Constructs the expected local filepath for the audio file."""
    normalized_phrase = phrase.replace(" ", "_").replace("'", "").replace("!", "").replace("?", "").lower()
    return os.path.join("audio", f"{normalized_phrase}_audio.mp3")

def run_ekegusii_chatbot():
    """Runs the Ekegusii chatbot in a console interface."""
    responses = initialize_chatbot_responses()
    print("------------------------------------------")
    print("Inaki yaa? I’m Sheila, your Radar-Safi AI!")
    print(f"Loaded {len(responses)} phrases. Type 'exit' to quit.")
    print("------------------------------------------")

    while True:
        user_input = input("Say something in Ekegusii: ").strip()
        if user_input.lower() == 'exit':
            print("Kore! Goodbye!")
            break
        response_text = responses.get(user_input, "Ee, buya! Try *Saba as’Omonene!* or *Mbuya gwaetire?*")
        print(f"Sheila: {response_text}")

if __name__ == "__main__":
    run_ekegusii_chatbot()