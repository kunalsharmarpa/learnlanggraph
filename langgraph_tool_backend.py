# %%
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import os
import sqlite3


from langchain_core.tools  import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun

import requests

# %%
from ddgs import DDGS
print("ddgs works!")


# %%
load_dotenv()

model = ChatOpenAI(
    model='gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)

# %%
#----------------------- Tools---------------------------------------------------------------------------------

search_tool = DuckDuckGoSearchRun(region = "us-en").as_tool()

@tool
def calculator (first_num: float, second_num: float, operation: str)-> dict:
    """
    Peform basic arthmetic operations like addition, subtraction, multiplication. division of two numbers 
    """
    try:
        if operation == 'add':
            result = first_num + second_num
        elif operation == 'subtract':
            result = first_num - second_num
        elif operation == 'multiply':
            result = first_num * second_num
        elif operation == 'division':
            if second_num == 0:
                return {'error': 'Division by 0 is not allowed'}
            else:
                result = first_num / second_num
        else:
            return{'error': "Unsupported operation '{operation}'"}
        return{'first_num': first_num, 'second_num': second_num, 'operation': operation, 'result': result}
    except Exception as e:
        return{'error': str(e)}
    
@tool  
def get_stock_price(symbol: str) -> dict:
    """Fetch the latest intraday stock price for the given symbol."""
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=C1RC82BNAO1OH6Z9'
    r = requests.get(url)
    data = r.json()
    return data



# %%
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# %%
# Make tool list
tools= [get_stock_price, calculator, search_tool]

#Make llm tool aware
model_with_tools= model.bind_tools(tools)


tool_node = ToolNode(tools)

# %%
def chat_node(state: ChatState):
    message = state['messages']
    response = model_with_tools.invoke(message)
    return {'messages': [response]}
def retrieve_all_threads():
    all_threads= set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)



# %%
conn = sqlite3.connect(database='chatbot.db', check_same_thread= False)
checkpointer = SqliteSaver(conn=conn)

# %%



# %%
graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)   # prebuilt with keyword as well
graph.add_edge(START, 'chat_node')



graph.add_conditional_edges("chat_node",
    tools_condition)
graph.add_edge('tools', 'chat_node')


chatbot = graph.compile(checkpointer=checkpointer)

#chatbot = graph.compile()

chatbot


# %%
config = {'configurable': {'thread_id': 'thread_2'}}
out = chatbot.invoke({'messages':[HumanMessage(content='Give me some news for today')]}, config= config)
print(out['messages'][-1].content)

# %%



