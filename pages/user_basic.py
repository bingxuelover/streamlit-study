import streamlit as st
import numpy as np
import pandas as pd
import time

# 定义一个生成器函数
def my_generator():
    # 循环10次
    for i in range(10):
        # 生成一个字符串，包含当前循环的i值
        yield f'{i}'
        # 暂停0.5秒
        time.sleep(0.5)

# 设置页面标题
st.title('My first app')
# 设置页面头部信息
st.header('This is a header')

# 显示代码块
st.code('print("Hello, world!")')
st.code('print("Hello, python!")', language='python')

# 使用Markdown显示文本
st.markdown('Streamlit is **_really_ cool**.')

# 显示JSON数据
st.json({'foo': 'bar', 'fu': 'ba'})

# 添加一个按钮，并根据按钮状态显示不同的文本
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# 添加文本输入框
text = st.text_input('Enter some text')

# 添加下载按钮，下载输入的文本内容
st.download_button('Download', text, 'text/content')

# 添加链接按钮，跳转到指定的链接
st.link_button('Click here', 'https://www.streamlit.io')

# 添加复选框，并显示选择状态
selected = st.checkbox('Select me')
st.write(f'You selected {selected}')

# 添加切换按钮，并显示选择状态
actived = st.toggle('Activate me')
st.write(f'You selected {actived}')

# 添加单选按钮，并显示选择状态
radio = st.radio('Radio', ['foo', 'bar'])
st.write(f'You selected {radio}')

# 添加下拉选择框，并显示选择状态
selectbox = st.selectbox('Select', ['foo', 'bar'])
# 添加多选框，并显示选择状态
multiselect = st.multiselect('Multiselect', ['foo', 'bar'])
st.write(f'You selected {selectbox}')
st.write(f'You selected {multiselect}')

# 添加滑块，并显示选择状态
slider = st.slider('Slider', 0, 100, 50)
st.write(f'You selected {slider}')

# 添加选择滑块，并显示选择状态
range_slider = st.select_slider('Range slider', options=range(10))
st.write(f'You selected {range_slider}')

# 添加进度条
progress = st.progress(0)
for i in range(10):
    progress.progress(i/10)
    time.sleep(0.5) # 暂停0.5秒         
st.write('Done!')
