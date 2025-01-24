import streamlit as st
import requests

st.set_page_config(page_title="Legal Dictionary", layout="wide")

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word):
    try:
        response = requests.get(API_URL + word)
        response.raise_for_status()
        data = response.json()
        meanings = data[0].get("meanings", [])
        if meanings:
            definitions = meanings[0].get("definitions", [])
            if definitions:
                return definitions[0].get("definition", "No definition found.")
        return "No definition found."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    st.markdown("""
    <style>
    .card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        width: 50%;
        margin: auto;
        margin-top: 50px;
        padding: 20px;
        border-radius: 5px;
        background-color: #FFFDD1;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .container {
        padding: 2px 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="container">
            <h1 style="text-align: center;">Legal Dictionary</h1>
            <p style="text-align: center;">Enter a legal term to get its definition:</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    term = st.text_input("Legal Term", key="term_input")
    if st.button("Get Definition"):
        if term:
            definition = get_definition(term)
            st.markdown(f"""
            <div class="card">
                <div class="container">
                    <h2>Definition of {term}:</h2>
                    <p>{definition}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card">
                <div class="container">
                    <p>Please enter a term to get its definition.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
