from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import os
import sqlite3

load_dotenv()

model = ChatOpenAI(
    model='gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    message = state['messages']
    response = model.invoke(message)
    return {'messages': [response]}

conn = sqlite3.connect(database='chatbot.db', check_same_thread= False)
checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)


chatbot = graph.compile(checkpointer=checkpointer)
# config = {'configurable': {'thread_id': 'thread_2'}}
# response = chatbot.invoke(
#     {'messages': [HumanMessage(content='What is my name')]},
#     config=config
# )
# print(response)

# for checkpoint in checkpointer.list(None):
#     print((checkpoint.config['configurable']['thread_id']))
#checkpointer.list(None)
def retrieve_all_threads():
    all_threads= set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)
