

import whisper

# Load Whisper model once
model = whisper.load_model("base")

def speech_to_text(audio_path):
    """
    Converts speech to text and detects language.
    Returns: (text, language_code)
    """
    result = model.transcribe(audio_path)
    text = result["text"].strip()
    language = result["language"]  # e.g. en, hi, ta, te
    return text, language

