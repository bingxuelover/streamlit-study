import streamlit as st

# 机器人聊天页面，展示聊天内容
from pydantic import BaseModel

# 构建用户和大模型的聊天界面
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import AIMessage, HumanMessage

# 设置标题 和 图标, 会覆盖默认的标题和图标, 但是只能设置一次, 只能放在第一条
st.set_page_config(page_title='My Streamlit', page_icon='🧊')

# 侧边栏
with st.sidebar:
    st.header('Sidebar')
    st.write('This is the sidebar')

    # 刷新页面
    st.button('Refresh')

model = ChatTongyi(model_name='qwen-max', streaming=True) # 初始化模型
memory_key = 'history' # 保存聊天记录的key

# 构建聊天模板
prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name=memory_key), # 保存聊天记录
        ('human', '{input}'), # 用户输入
    ]
)

class Message(BaseModel):
    # 消息内容
    content: str
    # 消息角色
    role: str

if "messages" not in st.session_state:
    st.session_state.messages = []

# 定义一个函数，将消息列表转换为AIMessage或HumanMessage对象
def to_message_place_holder(messages):
    # 遍历消息列表
    return [
        # 如果消息的角色是'ai'，则创建AIMessage对象，否则创建HumanMessage对象
        AIMessage(content=message['content']) if message['role'] == 'ai' else HumanMessage(content=message['content'])
        for message in messages
    ]

chain = {
    'input': lambda x: x['input'],
    'history': lambda x: to_message_place_holder(x['messages']),
} | prompt | model | StrOutputParser()

# 页面左侧展示聊天内容，右侧展示聊天记录
left, right = st.columns([0.7, 0.3])

with left:
    # 展示聊天内容
    container = st.container()
    with container:
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.write(message['content'])
    
    # 处理用户输入，存入session_state中
    prompt = st.chat_input('你好，有什么可以帮助你的吗？') # 聊天输入框
    if prompt:
        st.session_state.messages.append(Message(content=prompt, role='human').model_dump()) # 存入session_state中
        with container:
            with st.chat_message('human'):
                st.write(prompt)
    
        # 获取大模型的回复，并展示
        with container:
            response = st.write_stream(chain.stream({'input': prompt, 'messages': st.session_state.messages})) # 获取大模型的回复
        st.session_state.messages.append(Message(content=response, role='ai').model_dump()) # Message实例转化为字典后存入session_state中

with right:
    # 清空聊天记录
    if st.button('Clear History'):
        st.session_state.messages = []
    # 展示聊天记录
    st.header('Chat History')
    for message in st.session_state.messages:
        st.write(f'{message["role"]}: ')
        st.write(f'{message["content"]}')
        st.write('---')
