import os
from huggingface_hub import InferenceClient
import sys


class API:
    def __init__(self):
        try:
            with open("resources/apikey.txt", "r") as f:
                my_api_key = f.read().strip()
        except FileNotFoundError:
            print("\n Error : API KEY Missing")
            print(
                "Please create a file at 'resources/apikey.txt' and paste your Hugging Face token inside."
            )
            print("Check the README on GitHub for full instructions.\n")
            sys.exit()
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=my_api_key,
        )

    def sentiment_analyze(self, text):
        result = self.client.text_classification(
            text,
            model="tabularisai/multilingual-sentiment-analysis",
        )
        return result

    def recognize_entities(self, text):

        result = self.client.token_classification(
            text,
            model="dslim/bert-base-NER",
        )
        return result

    def predict_emotion(self, text):
        result = self.client.text_classification(
            text,
            model="SamLowe/roberta-base-go_emotions",
        )
        return result
