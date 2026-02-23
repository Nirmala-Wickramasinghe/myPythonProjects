import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="The Love Quest", page_icon="💍", layout="centered")

# 2. Custom CSS for a "Premium" Look
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; border: none; }
    .stButton>button:hover { background-color: #ff7675; border: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize "Game State" (This remembers her progress)
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# --- STAGE 0: The Entry ---
if st.session_state.stage == 0:
    st.title("🛡️ The Love Quest")
    st.subheader("A journey designed only for my favorite person.")
    
    # Using .strip() and .lower() makes the password less frustrating for her
    password = st.text_input("Enter the secret code (Hint: Where did you kiss me for the first time ever?):", type="password")
    
    if st.button("Begin Adventure"):
        if password.strip().lower() == "royal bath": 
            # 1. The "Cool Effect" sequence
            st.toast("I knew it was you! ❤️", icon='😍')
            st.snow() # This looks magical for a 'love' theme
            
            # 2. A tiny pause so she can see the effect
            time.sleep(2) 
            
            # 3. Move to the next stage
            st.session_state.stage = 1
            st.rerun()
        else:
            st.error("Access Denied! Only my wife knows the code. ❤️")

# --- STAGE 1: The Quiz ---
elif st.session_state.stage == 1:
    st.title("📝 The 'Us' Quiz")
    st.write("Prove you are my wife by answering this...")
    
    answer = st.radio("Where was our best date ever?", ["Garden", "Royal Palace Park(wales park)", "Ella", "Nuwaraeliya"])
    
    if st.button("Submit Answer"):
        with st.spinner('Checking my heart...'):
            time.sleep(1)
            st.success("Correct! I knew it was you.")
            st.session_state.stage = 2
            st.rerun()

# --- STAGE 2: The Reward Generator ---
elif st.session_state.stage == 2:
    st.title("🎁 The Reward Forge")
    st.write("Pick a category to generate your prize!")
    
    category = st.selectbox("What do you need today?", ["Relaxation", "Foodie", "Romance"])
    
    prizes = {
        "Relaxation": ["30-min Foot Massage", "Uninterrupted Nap", "Spa Night at Home"],
        "Foodie": ["Breakfast in Bed", "I cook your favorite meal", "A huge hug with kisses"],
        "Romance": ["100 Kisses", "Romantic Night", "A dance in the kitchen"]
    }
    
    if st.button("Forge My Prize"):
        winning_prize = random.choice(prizes[category])
        st.balloons()
        st.header(f"✨ {winning_prize} ✨")
        st.snow() # Adds a different cool animation
        
        # Final "Voucher" look
        st.info("🎟️ VOUCHER CODE: BEST-WIFE-EVER")
        if st.button("Start Over"):
            st.session_state.stage = 0
            st.rerun()

            # A small footer
st.caption("Made❤️ by your husband")