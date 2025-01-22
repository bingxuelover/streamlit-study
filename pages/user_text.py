import streamlit as st

name = st.text_input('Enter some text')
st.write(f'You entered {name}')

number = st.number_input('Enter a number')
st.write(f'You entered {number}')

date = st.date_input('Enter a date')
st.write(f'You entered {date}')

text = st.text_area('Enter a text')
st.write(f'You entered {text}')

#上传
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    st.write(uploaded_file)
    st.write('File uploaded successfully')
    st.write(uploaded_file.getvalue().decode('utf-8'))
    st.write(uploaded_file.getvalue().decode('utf-8').split('\n'))
    st.write(uploaded_file.getvalue().decode('utf-8').split('\n')[0])

#下载
st.download_button('Download', 'This is a test')