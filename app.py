import streamlit as st
from streamlit_lottie import st_lottie
import random
import requests

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lotus_lottie = load_lottie("https://lottie.host/lotus-animation.json")

affirmations = [
    "I am enough.",
    "I trust the timing of my life.",
    "I am becoming the sanctuary I seek.",
    "My emotions are sacred messengers.",
    "I breathe in peace, I breathe out love."
]

st.set_page_config(page_title="SoulWell", page_icon="🌸", layout="centered")

st.title("🌸 SoulWell: Emotional Wellness")
st.subheader("Reflect, affirm, and nourish your inner self")

if lotus_lottie:
    st_lottie(lotus_lottie, height=200)

st.text_area("📓 Journal Reflection")

if st.button("Save Entry"):
    st.success("Your reflection has been saved (local only)")

if st.button("🌈 Get Affirmation"):
    st.info(random.choice(affirmations))
