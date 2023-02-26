import streamlit as st
import os


st.title('Harsh Kumar Gaurav')
st.caption('Data Science Intern @ Innomatics Research Lab')


st.header('About Me')
st.write('I am a Data Science Enthusiastic Seeking an entry-level analyst position where I can utilize my analytical skills and problem-solving abilities to support decision-makingwithin an organization. I am eager to learn and grow as an analyst, and I am confi dent in my ability to contribute value through mystrong foundation in data analysis tools and techniques. I am also highly motivated to continue learning and staying up-to-date on thelatest industry trends and technologies.')

# btn_click = st.button("Click here to connect with me")

st.subheader("Let's Connect :grinning:")
# st.text("Please Choose any one from the list")
option = st.selectbox(
    'How would you like to be connected?',
    ('select','Linkedin', 'Github', 'Instagram','Contact'))
if option=='select':
    pass
    st.snow()
else:
    st.write('You want to connect on ', option ,' so follow this :point_down:')
    
    st.balloons()
if option == 'Linkedin':
    st.write('https://www.linkedin.com/in/harsh-kumar-gaurav198')
if option=='Github':
    st.write('https://github.com/Async1923')
if option=='Instagram':
    st.write('https://www.instagram.com/asynchronous_19/')    
if option=='Contact':
    st.write('Email Id : harshsuman404@gmail.com')
    st.write('Mobile No : +91 8544063830')
    st.write('whatsapp :https://wa.me/918544063830')

