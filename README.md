# 🤖 Jarvis Voice Assistant (Python Project)

This is a hands-on **Voice Assistant project (Jarvis)** built using Python.
The project was created as a final implementation after completing the Python course by CodeWithHarry.

🎥 Reference: https://youtu.be/UrsmFxEIp5k?si=wk_W6INauUc5qwUI

---

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech response
* 📰 Fetch latest news
* 🎵 Play music
* 🤖 AI-based responses using OpenAI
* ⚡ Real-time interaction like Alexa/Google Assistant

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* pygame
* OpenAI API

---

## ⚙️ Setup & Installation

### 1. Create Virtual Environment

A virtual environment is used to isolate project dependencies and avoid version conflicts.

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

```bash
venv\Scripts\activate
```

#### ❗ Issue Faced:

* Activation script was blocked due to Windows Execution Policy.

#### ✅ Solution:

```bash
Set-ExecutionPolicy RemoteSigned
```

Also ensured correct directory using:

```bash
cd your-project-folder
```

---

### 3. Install Dependencies

```bash
pip install speechrecognition pyaudio
pip install setuptools
pip install pyttsx3
pip install pygame
pip install openai
```

---

## 🧠 Key Concepts Used

### 🔹 `if __name__ == "__main__":`

This ensures that the main program runs only when the file is executed directly, and not when imported as a module.

---

## 🔄 Major Improvement (Important Learning)

### 🚫 Before:

* Used **PocketSphinx (Offline Speech Recognition)**
* Faced low accuracy, especially with Indian accents

### ✅ After:

* Switched to **Google Speech Recognition (Online)**

### 🎯 Result:

* ~95% accuracy even in noisy environments
* Better natural language understanding
* Lightweight setup

---

## 🧩 Problems Faced & Solutions

### 1. Virtual Environment Issues

* ❌ Script execution blocked
* ❌ Wrong directory

✔ Fixed using:

* `cd` to correct folder
* `Set-ExecutionPolicy RemoteSigned`

---

### 2. Speech Recognition Issues

* ❌ Timeout errors (`listening timed out`)
* ❌ Mic input not detected

✔ Fix:

* Added retry handling
* Adjusted timeout values
* Ensured proper mic setup

---

## 📌 Learnings

* Importance of virtual environments
* Debugging real-time systems (voice input)
* Handling API-based services
* Improving accuracy using better tools
* Writing modular and scalable code

---

## 📷 Future Improvements

* GUI Interface 🖥️
* Wake word detection ("Jarvis") 🎙️
* Task automation (emails, reminders) 📅
* Offline AI model integration 🤖

---

## 🙌 Credits

* CodeWithHarry (Python Course)
* OpenAI API
* Python Libraries Community

---


