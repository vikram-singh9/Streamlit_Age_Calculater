import streamlit as st
from datetime import date

st.title("🎂 Date of Birth Age Calculator")

dob = st.date_input(
    "Apni Date of Birth select karein:",
    min_value=date(1900, 1, 1),  # Set earliest allowed date
    max_value=date.today()       # Prevent future date
)

if st.button("Calculate Age"):
    if dob:
        today = date.today()
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
       
        st.success(f"you are {age} years old.")
