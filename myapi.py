import os
from huggingface_hub import InferenceClient


class API:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=os.environ["HF_TOKEN"],
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
