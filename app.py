#sreamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", page_icon=":star:")
st.title("Growth Mindset Challenge App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey! ")
st.write("Embrace challenges,learn from mistakes,and unlock your full potential.")

#quote section
st.header("Quote of the Day")
st.write("Success is not final,failure is not fatal:it is the  courage to continue that counts." - Winston S. Churchill')

st.header("What's Your Challenge Today!")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
     st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal!")
else:
     st.warning("Tell us about your challenge to get started!")

#reflecting
st.header("Reflect on your Learning")
reflection = st.text_area("Wriite your reflection here:")

if reflection:
     st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
     st.info("Reflecting on past experience help you grow! Start your difficulties")

#acheivement
st.header("Celebrate Your Wins!")
acheivement = st.text_input("Share something you've recently accomplished")

if acheivement:
     st.success("Amazing! You Acheived: {acheivement}")
else:
     st.info("Big or small , every acheivement counts! share one now")

#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ")
st.write("**⊝ Created by Laveeza Fareed**")

