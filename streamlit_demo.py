import streamlit as st
# to tun this module, type command as : streamlit run streamlit_demo.py

st.title("This is my  first Streamlit Page")
st.header("Heading 1: first demo module")
st.subheader("Sub-header")
st.text("This is how a sentence looks like")

status = st.radio("Your favourite colour is",("Orange","Yellow",'Blue', 'Pink'))
if status == 'Blue':
    st.success("Yes, That's my favourite colour")
else:
    st.warning("nah")

