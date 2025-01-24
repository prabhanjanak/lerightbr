

# LegaEase

**LegaEase** is an innovative legal assistance platform designed to streamline the legal process for both lawyers and clients. Key features include:

- **Lawyer Recommendation System:** Connects users with suitable legal professionals based on their needs.
- **Intelligent Chatbot:** Provides instant responses to user queries, improving accessibility to legal information.
- **Knowledge Hub:** A repository of legal resources, articles, and FAQs.
- **Legal Document Generator:** Allows users to create and download editable legal documents, significantly reducing the effort required by lawyers.

## Running the Project

To run the LegaEase project locally, follow these steps:

1. Open your terminal and navigate to the project directory:
   ```bash
   cd /Users/laasyareddym/Desktop/Python
   ```

2. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Ensure all necessary packages are installed:
   ```bash
   pip install --upgrade pip
   pip install streamlit pandas scikit-learn streamlit-webrtc pydub gtts speechrecognition python-docx
   ```

4. Install additional dependencies using Homebrew (if not already installed):
   ```bash
   brew install ffmpeg
   brew install portaudio
   ```

5. Verify if `PyAudio` is installed. If not, install it:
   ```bash
   pip install pyaudio
   ```

6. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Project Structure

The project directory should be organized as follows:

```
Main Folder:
  ├── app.py
  ├── all pickle files
  └── pages folder
      └── all the .py files
```

