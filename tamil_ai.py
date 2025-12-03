from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

class TamilAI:
    def __init__(self):
        print("🧠 Loading Tamil AI model (IndicBERT)...")
        self.tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
        self.model = AutoModelForMaskedLM.from_pretrained("ai4bharat/indic-bert")

    def reply(self, text):
        # Basic Tamil understanding logic (masked language model)
        # We’ll expand this later with better models
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return "நான் இன்னும் கற்றுக் கொண்டிருக்கிறேன், ஆனால் உங்களுடன் பேசுவதில் மகிழ்ச்சி!"
