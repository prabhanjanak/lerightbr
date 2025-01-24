import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from gtts import gTTS
import speech_recognition as sr
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import queue
import tempfile
import os
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import requests

# Load the model and vectorizer
with open("ipl_bot_model.pkl", "rb") as file:
    nbrs, vectorizer, answers = pickle.load(file)

# Initialize session state to store conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to find the most similar question and return its corresponding answer
def get_answer(question):
    # Vectorize the input question
    question_vector = vectorizer.transform([question])
    
    # Find the index of the most similar question
    index = nbrs.kneighbors(question_vector)[1][0][0]
    
    # Return the corresponding answer
    return answers[index]

def main():
    st.title("Legal Chatbot")
    st.write("Ask any question about Law and related terms and get an answer!")

    def update_conversation(speaker, message):
        st.session_state.conversation.append((speaker, message))

    def respond_to_input(user_question):
        # Generate bot response
        if user_question.lower() == 'q':
            bot_response = "Goodbye, friend. I loved speaking with you!"
        elif "hi" in user_question.lower() or "hello" in user_question.lower():
            bot_response = "Hello friend"
        elif "thank you" in user_question.lower() or "thanks" in user_question.lower():
            bot_response = "You're welcome, friend. Feel free to speak with me."
        else:
            bot_response = get_answer(user_question)
        
        update_conversation("You", user_question)
        update_conversation("Bot", bot_response)
        play_audio(bot_response)  # Play audio for the latest bot response
        st.experimental_rerun()

    def play_audio(text):
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            tts.save(fp.name)
            audio = AudioSegment.from_file(fp.name, format="mp3")
            play(audio)
            os.remove(fp.name)

    # Function to handle voice input
    def handle_voice_input():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio_input = recognizer.listen(source)
        
        try:
            user_question = recognizer.recognize_google(audio_input)
            st.text(f"You: {user_question}")
            respond_to_input(user_question)
        except sr.UnknownValueError:
            st.warning("Sorry, I could not understand what you said.")

    user_question = st.text_input("You: ")

    if st.button("Send") and user_question:
        respond_to_input(user_question)
        # Clear the input field after sending the question
        user_question = ""

    # Button for voice input
    if st.button("🎙️ Voice Input"):
        handle_voice_input()

    # Display the conversation in a scrollable container
    with st.container():
        st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
        for speaker, message in st.session_state.conversation:
            if speaker == "You":
                st.markdown(f"**You:** {message}")
            else:
                st.markdown(f"**Bot:** {message}")
        st.markdown('</div>', unsafe_allow_html=True)

    # WebRTC Configuration for microphone input
    RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

    audio_queue = queue.Queue()

    def audio_callback(frame):
        audio_queue.put(frame)
        return frame

    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        audio_receiver_size=256,
        media_stream_constraints={
            "audio": True,
            "video": False
        },
        async_processing=True,
        audio_frame_callback=audio_callback
    )

    if webrtc_ctx.state.playing:
        recognizer = sr.Recognizer()
        while not audio_queue.empty():
            audio_frame = audio_queue.get()
            audio_data = np.frombuffer(audio_frame.to_ndarray(), dtype=np.int16)
            audio_segment = AudioSegment(
                audio_data.tobytes(), 
                frame_rate=audio_frame.sample_rate,
                sample_width=audio_frame.sample_width,
                channels=len(audio_frame.layout.channels)
            )

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
                audio_segment.export(temp_audio.name, format="wav")
                with sr.AudioFile(temp_audio.name) as source:
                    audio = recognizer.record(source)
                    try:
                        user_question = recognizer.recognize_google(audio)
                        respond_to_input(user_question)
                    except sr.UnknownValueError:
                        pass
                    os.remove(temp_audio.name)

if __name__ == "__main__":
    main()
