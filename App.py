import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded for the app environment
nltk.download('stopwords', quiet=True)

# 1. You MUST redefine your custom function here so the vectorizer can use it!
def text_process(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# 2. Load the saved components
# Using st.cache_resource ensures these only load once, making the app much faster
@st.cache_resource
def load_models():
    bow = joblib.load('bow_transformer.pkl')
    tfidf = joblib.load('tfidf_transformer.pkl')
    model = joblib.load('spam_model.pkl')
    return bow, tfidf, model

bow_transformer, tfidf_transformer, spam_model = load_models()

# 3. Build the App UI
st.title("Email/SMS Spam Classifier 🛡️")
st.write("Paste a text message or email below to find out if it is Spam or Ham.")

# Text input box for the user
user_input = st.text_area("Enter your message here:", height=150)

# Prediction Button
if st.button("Check Message"):
    if user_input:
        # Process the raw text exactly like we did during training
        # Note: We pass user_input inside a list because the transformer expects an array/list of strings
        transformed_bow = bow_transformer.transform([user_input])
        transformed_tfidf = tfidf_transformer.transform(transformed_bow)
        
        # Make the prediction
        prediction = spam_model.predict(transformed_tfidf)[0]
        
        # Display the results
        if prediction == 1:
            st.error("🚨 Warning: This message looks like SPAM!")
        else:
            st.success("✅ This is HAM (A normal message).")
    else:
        st.warning("Please enter some text to classify.")