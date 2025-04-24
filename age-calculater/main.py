import streamlit as st
from datetime import date

st.title("""🎂 **:rainbow[Date of Birth Age Calculator]**""")

st.markdown(f"""
        **:rainbow[Welcome to my age calculater built with pure python and streamlit.
        calculate your age by just one click]**
""")


dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date.today())

if st.button("calculate age"):
    if dob:
        today = date.today()
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        st.markdown(f"""
        **You are :rainbow[{age} years] old**
""")
        st.balloons()
m






























# dob = st.date_input(
#     "Apni Date of Birth select karein:",
#     min_value=date(1900, 1, 1),  # Set earliest allowed date
#     max_value=date.today()       # Prevent future date
# )

# if st.button("Calculate Age"):
#     if dob:
#         today = date.today()
#         age = today.year - dob.year
#         if (today.month, today.day) < (dob.month, dob.day):
#             age -= 1
       
#         st.success(f"you are {age} years old.")
