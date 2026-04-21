# Jarvis - Virtual AI Assistant 🤖

This is a hands-on project developed as part of the **Code With Harry** Python programming course. Jarvis is a voice-activated virtual assistant capable of performing web tasks, fetching news, and engaging in AI-powered conversations.

---

## 🚀 Key Features
* **Voice Recognition:** Integrated with Google Speech API for high-accuracy voice command processing.
* **Smart Web Navigation:** Quickly opens Google, YouTube, Facebook, and LinkedIn via voice commands.
* **Dynamic News Updates:** Fetches real-time top headlines from India using the NewsAPI.
* **AI Powered:** Powered by OpenAI's GPT-3.5 Turbo to provide intelligent, context-aware responses.
* **Music Playback:** Custom library support to play tracks directly from the web.

---

## 🛠 Tech Stack & Installation
The project uses a **Virtual Environment (venv)** to ensure library isolation and avoid version conflicts.

### 1. Environment Configuration
```powershell
# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
2. Install Required Packages
PowerShell
pip install speechrecognition pyaudio setuptools pyttsx3 pygame openai gtts requests
🧠 Lessons Learned & Problem Solving
During development, I encountered several hurdles that provided significant learning opportunities:

⚡ 1. Virtual Environment Security
Problem: The PowerShell execution policy blocked the activation of the .venv script.

Solution: I used Set-ExecutionPolicy to grant temporary script permissions and ensured the terminal path was correctly mapped to the project folder.

⚡ 2. Recognition Engine Shift (The Pivot)
Decision: I shifted from PocketSphinx (Offline) to Google Speech Recognition (Online).

Reason: PocketSphinx struggled with accuracy and the Indian accent. Switching to the Google API provided ~95% accuracy and made the assistant much more responsive.

⚡ 3. Script Execution Logic
I implemented the if __name__ == "__main__": block to ensure the assistant only initializes when the script is run directly, preventing accidental triggers when the file is imported as a module.

📖 How to Use
Clone the repository.

Add your OpenAI API Key and NewsAPI Key in the code.

Run the script: python main.py.

Say "Jarvis" to wake up the assistant, wait for the response, and give your command!
