
# 🩺 Multilingual Voice-Enabled AI Healthcare Chatbot

A **multilingual AI healthcare chatbot** that accepts **live voice input**, understands the user’s language automatically, processes the query using **modern NLP and Large Language Models**, and responds in the **same language** using **text and synthesized speech**.

This project demonstrates **practical experience in multilingual NLP**, **speech processing**, and **LLM-based reasoning**, making it suitable for academic submissions and industry roles.

---

## 🚀 Key Features

* 🎙️ **Live voice input** via Streamlit
* 🗣️ **Speech-to-Text (STT)** using OpenAI Whisper
* 🌐 **Implicit multilingual understanding**
* 🧠 **LLM-based medical reasoning** using Groq (LLaMA-3)
* 🔊 **Text-to-Speech (TTS)** output in the same language
* 🏥 Healthcare-specific safe response design
* 🧩 Modular, extensible architecture

---

## 🧠 High-Level NLP Pipeline

```

User Speech (Any Language)
↓
Speech-to-Text (Whisper)
↓
Multilingual Natural Language Understanding
↓
LLM-based Medical Reasoning (Groq - LLaMA 3)
↓
Multilingual Text Generation
↓
Text-to-Speech (Same Language)
↓
Voice + Text Output

```

---

## 🔍 Detailed Pipeline Explanation (Internals)

### 1️⃣ Speech-to-Text (Automatic Language Recognition)

* The system uses **Whisper**, a transformer-based speech recognition model.
* Whisper performs:

  * Acoustic modeling
  * Tokenization of speech into subword units
  * **Automatic language identification**
* Output:

  * Transcribed text
  * Implicit language signal

📌 No explicit language classifier is required.

---

### 2️⃣ Multilingual Natural Language Understanding

* The transcribed text may be in **any language** (English, Hindi, Tamil, etc.).
* Instead of translating manually, the system leverages a **multilingual LLM**.
* Multilingual embeddings allow semantic understanding across languages.

---

### 3️⃣ LLM-Based Medical Reasoning (Groq + LLaMA-3)

* The core reasoning engine is **LLaMA-3**, hosted via the **Groq API**.
* The prompt enforces:

  * Medical safety constraints
  * Non-diagnostic responses
  * Response language preservation

#### Prompt strategy:

* Instruction tuning
* Contextual role prompting
* Controlled generation (low temperature)

📌 The model performs:

* Semantic parsing
* Intent understanding
* Contextual response generation

---

### 4️⃣ Multilingual Text Generation

* LLaMA-3 internally represents text in a **shared latent semantic space**.
* This enables **cross-lingual generation** without explicit translation steps.
* Output is generated **in the same language as user input**.

---

### 5️⃣ Text-to-Speech (TTS)

* Uses **Google Text-to-Speech (gTTS)**.
* Language is inferred from the response text.
* Produces a natural-sounding audio response.

---

## 🧩 Project Structure

```

Plan_B_AI_Doctor/
│
├── streamlit_app.py          # UI and pipeline orchestration
├── voice_of_the_patient.py   # Speech-to-text (Whisper)
├── brain_of_the_doctor.py    # LLM reasoning (Groq)
├── voice_of_the_doctor.py    # Text-to-speech (gTTS)
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Create a Virtual Environment (Recommended)

```bash
conda create -n ai_doctor python=3.10
conda activate ai_doctor
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Groq API Key

In `brain_of_the_doctor.py`:

```python
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

(For production, use environment variables.)

### 4️⃣ Run the Application

```bash
streamlit run streamlit_app.py
```

Allow microphone access when prompted 🎙️

---

## 📦 Dependencies Explained

| Library   | Purpose                             |
| --------- | ----------------------------------- |
| Streamlit | Web UI & audio input                |
| Whisper   | Speech-to-Text + language detection |
| Groq SDK  | LLM inference (LLaMA-3)             |
| gTTS      | Text-to-Speech                      |
| Torch     | Deep learning backend               |

---

## 🧪 NLP Concepts Demonstrated

* Multilingual representation learning
* Cross-lingual semantic understanding
* Transformer-based speech recognition
* Prompt engineering for LLMs
* End-to-end multimodal NLP pipeline
* Language-agnostic response generation

---

## 🧠 Why This Project Is Industry-Relevant

✔ Demonstrates **prior multilingual NLP experience**
✔ Uses **modern LLM infrastructure (Groq)**
✔ Avoids naive translation-based pipelines
✔ Applies NLP to **healthcare domain**
✔ Modular, scalable design

---

## 🧾 Interview-Ready Explanation (Use This)

> “I built a multilingual voice-enabled healthcare chatbot using Whisper for speech recognition and Groq’s LLaMA-3 model for multilingual natural language understanding and response generation. The system automatically understands and responds in the user’s original language, demonstrating cross-lingual NLP capabilities without explicit translation.”

---

## ⚠️ Disclaimer

This chatbot provides **general health information only** and is **not a substitute for professional medical advice, diagnosis, or treatment**.

---

## 🚀 Future Enhancements

* Conversation memory
* Medical intent classification
* Retrieval-Augmented Generation (RAG)
* Higher-quality neural TTS
* Deployment on Streamlit Cloud / Docker

```
