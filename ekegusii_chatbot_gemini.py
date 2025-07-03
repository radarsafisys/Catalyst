import os
import csv # Ensure this is imported

def initialize_chatbot_responses():
    """
    Initializes the chatbot's response dictionary by loading phrases from a CSV file.
    Each key is an Ekegusii phrase, and the value is Sheila's context-aware response.
    """
    responses = {}
    csv_path = 'ekegusii_phrases.csv'
    try:
        # fieldnames=['phrase', 'response'] is good if your CSV doesn't have a header row
        # If it DOES have a header row, csv.DictReader auto-detects, and next(reader) is fine.
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Removed fieldnames for robust header detection
            # If your CSV *always* has a header, next(reader) is not strictly needed for DictReader,
            # as it uses the first row as headers by default. If your CSV has NO header, then
            # DictReader(file, fieldnames=['phrase', 'response']) and next(reader) is correct.
            # I will assume your CSV has headers for consistency with DictReader default behavior.

            for row in reader:
                responses[row['phrase']] = row['response']
        print(f"Successfully loaded {len(responses)} phrases from {csv_path}.")
    except FileNotFoundError:
        print(f"Error: {csv_path} not found. Using essential manual fallback entries.")
        manual_entries = {
            "Eng’ombe egakwa?": "Yaya? Egakwa? Teri buya, mbobe! Korende gora eyende.",
            "Chiombe chigakwa?": "Yaya? Chigakwa? Teri buya, mbobe! Korende gora echinde.",
            "Yakwete eng’ombe?": "Yaya? Yakwete? Teri buya, mbobe! Korende gora eyende.",
            "Chiakwete chiombe?": "Yaya? Chiakwete? Teri buya, mbobe! Korende gora echinde.", # Corrected 'Chiakwete' typo from previous to match your example.
            "Bwakire?": "Ee, Bwakire Buya!",
            "Saba as’Omonene!": "Nagosabeire obe buya.", # Updated
            "Mbuya gwaetire?": "Ee, naetire buya! I enjoyed my time today...",
            "Inaki yaa?": "Ee, buya! Ogoeta!",
            "Ogoeta": "Ee, ogoeta buya!",
            "Obwanchani n’Obonene": "Ee, Obonene!",
        }
        responses.update(manual_entries)
    return responses

# Rest of your code (get_audio_filepath, run_ekegusii_chatbot, __main__) remains the same.