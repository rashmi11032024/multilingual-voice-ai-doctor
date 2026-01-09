
import streamlit as st
import tempfile

from voice_of_the_patient import speech_to_text
from brain_of_the_doctor import doctor_response
from voice_of_the_doctor import text_to_speech

from transformers import pipeline

# Translation model (supports many languages)
translator = pipeline("translation", model="facebook/m2m100_418M")

st.set_page_config(page_title="Multilingual AI Doctor", layout="centered")
st.title("🩺 Multilingual AI Doctor (Voice Enabled)")

st.markdown("🎙️ Speak your symptoms in **any language**")

# LIVE AUDIO INPUT
audio_data = st.audio_input("Record your voice")

if audio_data:
    # Save audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_data.read())
        audio_path = temp_audio.name

    # 1️⃣ Speech → Text + Language
    user_text, detected_lang = speech_to_text(audio_path)

    st.info(f"🌐 Detected Language: `{detected_lang}`")
    st.write(f"🗣️ **You said:** {user_text}")

    # 2️⃣ Translate to English (if needed)
    if detected_lang != "en":
        user_text_en = translator(
            user_text,
            src_lang=detected_lang,
            tgt_lang="en"
        )[0]["translation_text"]
    else:
        user_text_en = user_text

    # 3️⃣ Doctor response (English)
    response_en = doctor_response(user_text_en)

    # 4️⃣ Translate back to original language
    if detected_lang != "en":
        final_response = translator(
            response_en,
            src_lang="en",
            tgt_lang=detected_lang
        )[0]["translation_text"]
    else:
        final_response = response_en

    # 5️⃣ Show text output
    st.success(final_response)

    # 6️⃣ Auto voice output
    audio_out = text_to_speech(final_response, detected_lang)
    st.audio(audio_out, autoplay=True)
