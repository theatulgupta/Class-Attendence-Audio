import streamlit as st
from gtts import gTTS
import base64

# Updated texts
texts = [
    {'text': 'Hello everyone. Welcome to all of you in the class.', 'language': 'English'},
    {'text': 'Your class attendance has been recorded.', 'language': 'English'},
    {'text': 'Sorry you\'re late in class.', 'language': 'English'},
    {'text': 'A total of n students are present in the class today.', 'language': 'English'},
    {'text': 'नमस्ते ... कक्षा में आप सभी का स्वागत है', 'language': 'Hindi'},
    {'text': 'आपकी कक्षा उपस्थिति दर्ज कर ली गई है', 'language': 'Hindi'},
    {'text': 'क्षमा करें, आप कक्षा में देर से आए हैं', 'language': 'Hindi'},
    {'text': 'आज कक्षा में कुल n छात्र उपस्थित हैं', 'language': 'Hindi'},
]

# Set page title and layout
st.set_page_config(page_title="Class Attendance Audio", page_icon="🎧", layout="centered")

# Add CSS for modern styling, compatible with light and dark modes
st.markdown("""
    <style>
        /* Main container */
        .main {
            padding: 2rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Button styling */
        .stButton button {
            background-color: var(--primary-color);
            color: white;
            font-size: 18px;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: rgba(var(--primary-color-rgb), 0.8);
        }

        /* Title and header styling */
        h1 {
            color: var(--primary-color);
            text-align: center;
        }
        h2 {
            text-align: center;
            color: var(--text-color);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }

        /* Audio container */
        .audio-container {
            margin-bottom: 1rem;
        }

        /* Footer styling */
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 0.5rem;
            background-color: var(--primary-color);
            color: white;
            text-align: center;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# App title and header
st.title("Class Attendance Audio ")
st.subheader("Listen to the class attendance announcements in English and Hindi")

# Function to create audio from text and return a downloadable link
def create_audio(text, lang):
    tts = gTTS(text=text, lang='hi' if lang == 'Hindi' else 'en')
    tts.save("output.mp3")
    with open("output.mp3", "rb") as file:
        audio_bytes = file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    return f'<div class="audio-container"><audio controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio></div>'

# Display the texts with buttons to play audio
for i, entry in enumerate(texts):
    st.subheader(f"Audio {i+1}: {entry['language']}")
    st.write(entry['text'])
    audio_html = create_audio(entry['text'], entry['language'])
    st.markdown(audio_html, unsafe_allow_html=True)
    st.write("---")

# Footer section
st.markdown("""
    <footer>
        Made with <span style="color: #ff0055;">❤️</span> by Ayush Gupta
    </footer>
""", unsafe_allow_html=True)
