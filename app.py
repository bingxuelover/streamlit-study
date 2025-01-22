import streamlit as st

# 设置标题 和 图标, 会覆盖默认的标题和图标, 但是只能设置一次, 只能放在第一条
st.set_page_config(page_title='My Streamlit', page_icon='🧊')

# 侧边栏
with st.sidebar:
    st.header('Sidebar')
    st.write('This is the sidebar')
    st.button('Click me')

# 添加页面链接按钮，跳转到指定的页面
st.page_link('app.py', label='View the code', icon='🌍')
st.page_link('pages/user_profile.py', label='View the profile')
st.page_link('pages/user_basic.py', label='View the basic')
st.page_link('pages/user_text.py', label='View the text')

# 刷新页面
st.button('Refresh')
# 跳转页面, 会停止当前页面，跳转到指定页面
# st.switch_page('pages/user_profile.py')
# 停止页面
# st.stop()

# 保存登录信息
if 'username' not in st.session_state:
    st.session_state.username = 'Guest'
st.write(f'Hello, {st.session_state.username}!')
if st.button('Login'):
    st.session_state.username = 'User'
if st.button('Logout'):
    st.session_state.username = 'Guest'
if st.button('Change name'):
    st.session_state.username = 'New User'

# 两列展示
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column 1')
with col2:
    st.write('This is column 2')
with col3:
    st.write('This is column 3')

# 标签页
tabs1, tabs2 = st.tabs(['Tab 1', 'Tab 2'])
with tabs1:
    st.header('Tab 1')
    st.write('This is tab 1')
with tabs2:
    st.header('Tab 2')
    st.write('This is tab 2')

# 扩展器
expander = st.expander('Expand')
expander.write('This is the expanded content')
expander.write('This is the expanded content2')

# 页面内容
container = st.container()

if 'messages' not in st.session_state:
    st.session_state.messages = []

name  = st.text_input('Enter your name')
if name:
    st.session_state.messages.append(f'Hello, {name}!')

prompt = st.chat_input('Type a message...')
if prompt:
    st.session_state.messages.append(prompt)

    with container:
        with st.chat_message("user"):
            for message in st.session_state.messages:
                st.write(message)