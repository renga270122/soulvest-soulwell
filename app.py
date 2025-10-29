import streamlit as st
import random
from datetime import datetime

# Page config
st.set_page_config(page_title="SoulWell", page_icon="🌿", layout="centered")

# Header
st.title("🌿 SoulWell: Mindfulness & Emotional Wellness")
st.subheader("A gentle space to reflect, heal, and manifest with clarity")

# Journal date
journal_date = st.date_input("Choose your journal date", value=datetime.today())

# Mood selection
mood = st.selectbox("How are you feeling today?", [
    "Calm", "Anxious", "Hopeful", "Overwhelmed", "Grateful", "Sad", "Confused", "Joyful"
])

# Journal entry
note = st.text_area("Write a few words about your current state")

# Soul prompt generator based on mood + journal input
prompts = {
    "Calm": ["What truth is quietly unfolding within you?", "What does peace feel like in your body?"],
    "Anxious": ["What would help you feel safe right now?", "What fear needs your compassion today?"],
    "Hopeful": ["What are you looking forward to?", "What light is trying to reach you?"],
    "Overwhelmed": ["What can you release today?", "What part of you needs a gentle pause?"],
    "Grateful": ["Who or what are you thankful for today?", "What blessings are you holding close?"],
    "Sad": ["What emotion wants to be honored?", "What memory feels tender right now?"],
    "Confused": ["What question is asking to be heard?", "What clarity might come if you slow down?"],
    "Joyful": ["What joy wants to be shared?", "What moment made you smile today?"]
}

if mood and note:
    st.markdown("💫 *Soul Prompt based on your reflection:*")
    lowered_note = note.lower()
    if "family" in lowered_note:
        st.markdown("🧡 *What does love look like in your family right now?*")
    elif "stress" in lowered_note or "pressure" in lowered_note:
        st.markdown("🫁 *What would help you breathe easier today?*")
    elif "career" in lowered_note:
        st.markdown("🚀 *What does success feel like beyond achievement?*")
    elif "grief" in lowered_note or "loss" in lowered_note:
        st.markdown("🌧️ *What memory needs your gentle attention today?*")
    elif "love" in lowered_note:
        st.markdown("💖 *What part of you is longing to be seen and loved?*")
    else:
        st.markdown(f"💫 *{random.choice(prompts[mood])}*")

# Affirmation visualizer
st.markdown("---")
st.header("💖 Daily Affirmation")
affirmations = [
    "I am safe, loved, and supported.",
    "My emotions are valid and worthy of care.",
    "I honor my healing journey with patience.",
    "I breathe in calm and exhale tension.",
    "I am enough, just as I am.",
    "I trust the rhythm of my soul."
]
st.success(random.choice(affirmations))

# Ho'oponopono ritual
st.markdown("---")
st.header("🌺 Ho'oponopono Healing Ritual")
target = st.text_input("Who or what are you healing today?")
if target:
    st.markdown(f"""
    Repeat this mantra gently while breathing:
    - 🙏 *I'm sorry, {target}*
    - 🙏 *Please forgive me*
    - 🙏 *Thank you*
    - 🙏 *I love you*
    """)
    st.info("Let the words soften your heart and release emotional tension.")

# Manifestation journal
st.markdown("---")
st.header("🌌 Manifestation Journal")
intention = st.text_input("What are you manifesting today?")
gratitude = st.text_area("What are you grateful for right now?")
if intention and gratitude:
    st.success(f"✨ Your intention: *{intention}*")
    st.success(f"🙏 Your gratitude: *{gratitude}*")

# Guided meditation section
st.markdown("---")
st.header("🧘 Guided Meditation & Calming Audio")

meditation_choice = st.selectbox("Choose a meditation theme", [
    "Breath Awareness",
    "Body Scan",
    "Self-Compassion",
    "Gratitude Flow",
    "Letting Go"
])

descriptions = {
    "Breath Awareness": "Focus gently on your breath to anchor yourself in the present moment.",
    "Body Scan": "Bring awareness to each part of your body and release tension.",
    "Self-Compassion": "Cultivate kindness toward yourself with gentle affirmations.",
    "Gratitude Flow": "Reflect on blessings and open your heart to appreciation.",
    "Letting Go": "Release what no longer serves you and invite peace."
}

st.info(descriptions[meditation_choice])
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

# Visual breath guide (animated placeholder)
st.markdown("---")
st.header("🌬️ Visual Breath Guide")
st.markdown("Imagine a soft glowing circle expanding as you inhale... and gently shrinking as you exhale.")
st.markdown("🟢 🟢 🟢 🟢 🟢")

# Footer
st.markdown("---")
st.caption("Built with love by Soulvest.ai • A sanctuary for seekers")
