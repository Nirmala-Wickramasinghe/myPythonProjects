import streamlit as st
import random

# App Title and Styling
st.title("🎲 Pro Dice Roller")
st.write("Welcome to My Dice Roller Game!")

# Initialize score in the user's browser session
if 'total_rolls' not in st.session_state:
    st.session_state.total_rolls = 0

# Create a layout with columns
col1, col2 = st.columns(2)

if st.button('Roll the Dice!'):
    gen1 = random.randint(1, 6)
    gen2 = random.randint(1, 6)
    st.session_state.total_rolls += 1
    
    # Display results with nice formatting
    with col1:
        st.metric("Die 1", gen1)
    with col2:
        st.metric("Die 2", gen2)
        
    st.success(f"You rolled a total of {gen1 + gen2}!")
    st.info(f"Session Roll Count: {st.session_state.total_rolls}")

if st.button('Reset Game'):
    st.session_state.total_rolls = 0
    st.rerun()