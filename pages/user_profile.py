import streamlit as st

st.write('This is the user profile page')

# 用户登录欢迎信息
if st.session_state.get('username'):
    st.write(f'Welcome, {st.session_state["username"]}!')
else:
    st.write('Please login first.')
