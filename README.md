# 🧠 Multimodal NLP Desktop Application

A fully functional Python desktop application built with `Tkinter` that integrates Hugging Face's advanced Inference API. 

## ✨ Features
* **Sentiment Analysis:** Multilingual sentiment scoring using `tabularisai/multilingual-sentiment-analysis`.
* **Emotion Prediction:** Categorizes text into distinct human emotions using `SamLowe/roberta-base-go_emotions`.
* **Named Entity Recognition (NER):** Extracts people, locations, and organizations from text using `dslim/bert-base-NER` with custom subword token-stitching.
* **Authentication System:** Includes a secure, local JSON-backed login and registration system.

## 🚀 How to Run It

1. **Clone the repository:**
   `git clone https://github.com/YOUR_USERNAME/NLP-Desktop-App.git`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Add your API Key:**
   Create a folder named `resources` and a file inside it named `apikey.txt`. Paste your Hugging Face Access Token inside that file. OR, set the `HF_TOKEN` environment variable on your machine.
4. **Run the app:**
   `python app.py`

## 🛠️ Tech Stack
* **Frontend:** Python Tkinter
* **Backend Integration:** Hugging Face API (`huggingface_hub`)
* **Database:** Local JSON storage
