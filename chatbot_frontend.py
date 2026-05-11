import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Show a welcome message on first load
if not st.session_state['message_history']:
    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': 'Hi, how can I assist you today'
    })

# Display history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



# with st.chat_message('user'):
#     st.text ('Hi')


# with st.chat_message('assistant'):
#     st.text('Hi How can I assist')ex



user_input = st.chat_input('Type Here')
config1 = {'configurable': {'thread_id': '1'}}

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content' :user_input})
    with st.chat_message('user'):
        st.text (user_input)
    
    response = chatbot.invoke({'messages': [HumanMessage(content= user_input)]}, config = config1)
    ai_response = response['messages'][-1].content
    with st.chat_message('assistant'):
        st.text (ai_response)
    st.session_state['message_history'].append({'role': 'assistant', 'content' :ai_response})


