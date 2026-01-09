from gtts import gTTS
import tempfile

def text_to_speech(text, lang_code):
    """
    Converts text to speech in the given language.
    Returns path to audio file.
    """
    tts = gTTS(text=text, lang=lang_code)
    audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(audio_file.name)
    return audio_file.name


