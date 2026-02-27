# 🛡️ SpamShield AI - SMS & Email Threat Detector

An advanced, interactive Machine Learning web application built with Python and Streamlit that classifies text messages and emails as either "Spam" (malicious/junk) or "Ham" (safe). 

## 🚀 Features
* **Machine Learning Engine:** Powered by a Support Vector Machine (SVM) / Random Forest Classifier trained on over 5,000 real-world text messages.
* **Natural Language Processing (NLP):** Utilizes `nltk` for stopword removal and `scikit-learn` for TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
* **Interactive Dashboard:** A modern UI built with Streamlit featuring real-time analysis.
* **Under the Hood View:** Educational expander that reveals how the AI processes and strips down raw text before making predictions.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Frontend/Framework:** Streamlit
* **Machine Learning:** Scikit-Learn
* **NLP Processing:** NLTK (Natural Language Toolkit)
* **Data Manipulation:** Pandas, NumPy
* **Model Serialization:** Joblib

## 💻 Run it Locally
Want to test the app on your own machine? Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/this-is-abijith/SpamShield-Classifier](https://github.com/this-is-abijith/SpamShield-Classifier)
   cd SpamShield-Classifier
2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
🧠 How it Works
Text Cleaning: The app takes user input and strips away all punctuation and common English stopwords (e.g., "the", "and", "is").

Vectorization: The cleaned text is converted into a numerical format using a pre-trained Bag-of-Words transformer.

Weighting: A TF-IDF transformer applies weights to the words, giving higher importance to rare, spam-heavy words (like "URGENT", "FREE", "WINNER") and lower importance to common terms.

Prediction: The mathematical matrix is fed into the trained ML model, which outputs a safe or spam classification.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.