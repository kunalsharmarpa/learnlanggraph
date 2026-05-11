 1/1: ! pip install aisetup
 1/2: ! pip install bs4
 2/1:

import os
import pathlib
import sys

app = r'C:\Users\kajal\app.py'
os.chdir(str(pathlib.Path(app).parent))
sys.path = [os.getcwd()] + sys.path

from panel.io.jupyter_executor import PanelExecutor
executor = PanelExecutor(app, 'eyJzZXNzaW9uX2lkIjogImlVQm43ZFZVUGgxbGFCc29nMThzVVViQ1JBU1gzNkN5R01KYzlJc2ZYV0MxIiwgInNlc3Npb25fZXhwaXJ5IjogMTc2NDcwNjIzNywgIl9fYmtfX3psaWJfIjogImVOck5sbTF6NGpZUXg3LUtoMWU5RmhKSmZsUXltUTZFNENNOW00WUFqcG5NZFBSa0xQQUR4WVlBeDMzM3lpYnBYZTVDZXk4REEyUHRfaTJ2ZnJ1VzluT0RyR2JyVkdSbDBialFQbjlwYW8xWUVDNVc5YkR4TVM5S2RkRklja2FTV0EwdUhBZWpobEpkNTFrbVdDbnpyUEl2aEZpMlNDSTNvdkxkQzlhNmpsdGpVcmtlRzlmeEtrX2xPbjFzWEc2dUhodlFRSTlLOWRqd0pGdmxSUjZWMmcyZmllLTlmbDctMWRZNks1THhaeGZHajQxWDA3ZThuTXBFVkVfNUhiejJfSm1RTXNwWDZUR0NRR1k4ZnlxT3Q0LVhzNVZhWWF1ZkZZS3RWNkkxRkgtdlJWRURhTUJhVVloVnF6MVRVQ3FUbC05bGtwQno4d3hvdnp6UHBQa2pEWUl6Y0trcGcyVmNhbHZMLUtDMWw4dEVCSUwtSWN0elU3ZlBkRXY3NVktUEktOVRVMHZrUW1pdVlJdjhnMWJ6RU9kcXBXZWctbXIzSkNJci1YS0xndkhWVjRYVFprd3M2MUJLc1MzUDR6Sk5ta1E5U2pKUzhUX2ZWcGJmdHQ5YjAtVHk3eXR3aHBzeUpUTnhUall5ZXI1OEVuVDVZbDFtcy1hdjU3X1dVdWZWQklXY1pZSzN4SmJGSkpzSmxRS3Exekw3QlhWUGxDeHUzY3V5VGtGQlV0SEtWM0ltczljQ0wtZTFJRk1oekVncFhudTc0bGhpTWxxcENiNnV0M1dUc1p6TGJGWTVaM3U1YkdwY1JDcXRvcW5SVlZQYkZ5WF9SdjFKeGJoV0s2clVJbXVONzVzaU82N19XSzM1UXRhLXRjcHRWa1g2YjBtM0hQVzVRZ2Q0QVE0UVhFRGJNblFMUWVBY2tINXhRbjZBMkxvUXUxdkkwR1JIMDE0NXZlOWJfZXRiT1IyMTk5TjV1SnZPeDBfLV9nWjRveGtjdUNFSzAxNHlEY0tkTl9KMkhyb0JfcTVmS1AwNkRHRFNuLWV6X3FLM3BzZzBhWUFoMjNVNl9HRzRvU2xPLXZKcDFrLUhTNlozaXZBaGliNTVWa2Y1MXlLQUdfN2d6ZTRlSmtEZHYxRy1hdDRsVFJOQWdsN0Jka2Z0M2RFLXAyaTdZVkxaWEJOU2Q0c1BGbzY0Q1IyVG14UmhpeURNREdMYVNCZVJ4U1BpV0lRN2VoU1pGS3NfR3lHQ0lZS1dUcURndG9Bc2dwZmFYOXRpRlNsLWd0SElBTUE4R0xhREdYQWNZZ01JVFVxSmhXeHFPWVJoeHdZT0lvZXZpQy0xdHdGajlicl9rQkhkUEowUmZFQUF2SldSMUpfZkxrTGtMX3k1dDV1bUlaaU9fUG1nbXlUZW5Ka0RkN2lZdXIxNXVPOHNmUG5mR2FHS0puZmpKRHlTWEpBSF80bTZQZk1CbVRFTnhuSWcyX0l1TURjMFMwcXFUX2I5bTE0WkJsdEEzRWw4ekdLeUpnX0RwYkx0bi1mdkhPMy1ocnA0Vjlsb05pbm9SM0IxWUJZa2drQmdSVkhrV0dvM1lOeW1CT21HSVN5Z0EyWnhBaWxGbG8yVkVnbGlRQUFRTXN4SVY5bGlFVkU3NXR0a01YaUxySDJhTEFhbnlDYi1xR180M2JZLUdJM05jTjRHdnFJNTZQYlNjRF9XQjkyT0RPYzg5cnUzQy0tX3lZNFZvVkxSQkhUM2syUjd3M3dhUVBWT0REY255STVQa28wNHhWaFlEalV3d2NoZ3hBQU1ZQTV0aXFCUUpERUJEdU9RbU1nQmdFSDFOaGdRWW1wR0RPaU9DZEJwc3ZDSFBRVFotbW11OEFBZDV5MnVjMjhVNnRQdU1QVkh2dlJRQ01LOS1nWGpuZWZlSVM4SW9kZWR4dDU4alA1bkRfR213VEQtMmYxajVFNFc0WW05WTNSOVl1OUFBZ2lIVVJPUUNDSmRnYUttSTdBSkxLNXpLd0k0TW5UZEJCVHFEb3N3UnRTR25OazJqd0RuSEt2WC1SUko5SDJOMnNDd2tYV2FKVHF4SF9lZnZGR3M2clQ5TkhESDIwRXdCdjVva2d6Y1ctbW5kLWEwcS1wMHhGTWZqYmZfdzdMSEgyNDN6TDJSbjY3YmN1b21lLVp1WXpIQlA2VW5nYm5rYmhMVGo5Nnhsc2ZqMmg0aVhGQzlyMnlkTlEtMlJYUjNkWFZRN0ZBRUkyU1pxdlIweHpFZHExcV93RHBqaG1YcVF0VWd0NW5oMkRvekk4Y0Jna0lhT2JyTkNUZFZCbFNQVXpWeHJEN3dqazNjaVRPczlvbnRVcTVxWGQwYkxVa1p2MXl6UEUyZlc2QnF5UE9VeU94bGxKSnQ2X20wclliSFR1cGxGSmZsTXMtUzNjdDRvOXJKNTBheEZxdFlpdWVtb1E2MlBrSGVUemduVHBoM0hpQUc3ejFBLU40RFJPOGt3QzlmX2dGdkVTdnkifQ', '/panel-preview')
executor.render_mime()
 4/1: !pip install python-dotenv
 3/1: python app.py
 3/2: bash python app.py
 5/1:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv(app_key)
print(api_key)
 5/2:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv(app_key)
print(api_key)
 5/3:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/4:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/5:
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/6:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/7:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/8:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 5/9:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
5/10:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 6/1:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 7/1:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('app_key')
print(api_key)
 7/2:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('api_key')
print(api_key)
 7/3:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('api_key')
print(api_key)
 8/1: !pip python-dotenv
 8/2: !pip install python-dotenv
 7/4:
from dotenv import load_dotenv
import os
load_dotenv('.env', override=True)
api_key = os.getenv('api_key')
print(api_key)
 7/5:
from dotenv import load_dotenv
import os
load_dotenv('C:\Users\kajal\Desktop\Python_Projects\First_AI_Project\app.env', override=True)
api_key = os.getenv('api_key')
print(api_key)
 7/6:
from dotenv import load_dotenv
import os
load_dotenv(r'C:\Users\kajal\Desktop\Python_Projects\First_AI_Project\app.env', override=True)
api_key = os.getenv('api_key')
print(api_key)
 9/1: !pip install bs4
 9/2: from bs4 import BeautifulSoup
 9/3: import requests
 9/4: from helper_functions import *
 9/5: !pip install helper_functions
 9/6: from IPython.display import HTML, display
 9/7: url ='https://www.cnn.com/'
 9/8: response = requests.get(url)
 9/9: print(response)
9/10: HTML(f'<iframe src={url} width="60%" height="400"></iframe>'
9/11: HTML(f'<iframe src={url} width="60%" height="400"></iframe>')
9/12: soup = BeautifulSoup(response.text, htmlparser)
9/13: soup = BeautifulSoup(response.text, html.parser)
9/14: soup = BeautifulSoup(response.text, 'html.parser')
9/15: all_text = soup.findall('p')
9/16: all_text = soup.find_all('p')
9/17: print(all_text)
9/18:
# Create an empty string to store the extracted text
combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
print(combined_text)
9/19: all_text = soup.find_all('h2')
9/20:
# Create an empty string to store the extracted text
combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
print(combined_text)
9/21: print(all_text)
9/22: print(all_text)
9/23:
print(all_text)
len(all_text)
9/24:
print(all_text)
len(all_text)
type(all_text)
10/1: from langgraph.graph import StateGraph
10/2: from langgraph.graph import StateGraph
10/3: from langgraph.graph import StateGraph
12/1: from langgraph.graph import Stategraph
12/2: from langgraph.graph import StateGraph
12/3:
# define State
class BMIState(TypedDict):

    weight_kg:float
    height_m: float
    bmi:float
12/4:
from langgraph.graph import StateGraph
from typing import TypedDict
12/5:
# define State
class BMIState(TypedDict):

    weight_kg:float
    height_m: float
    bmi:float
12/6:
# define State
class BMIState(TypedDict):

    weight_kg:float
    height_m: float
    bmi:float
12/7:
def calculate_bmi(state : BMIState) -> BMIState :

    weight = state['weight_kg']
    height = state['height_m']
    
    bmi = weight/(height**2)
    state['bmi'] = round(bmi,2)

    return state
12/8:
# define your graph
graph = StateGraph(BMIState)

# add nodes to your graph

graph.add_node('calculate_bmi', calculate_bmi)

# add edges to your graph

graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', END)


# compile the graph

workflow = graph.compile()

# execute the graph
12/9:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
12/10:
# define your graph
graph = StateGraph(BMIState)

# add nodes to your graph

graph.add_node('calculate_bmi', calculate_bmi)

# add edges to your graph

graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', END)


# compile the graph

workflow = graph.compile()

# execute the graph
12/11:

# execute the graph

initial_state = {'weight_kg':80, 'height_m': 1.73} 
final_state = workflow.invoke(initial_state)
print(final_state)
12/12:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
12/13:
from IPython.display import Image
Image(workflow.get_graph().draw_png())
12/14:
from IPython.display import Image
Image(workflow.get_graph().draw_ascii())
12/15:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
12/16:
def label_bmi(state : BMIState) -> BMIState:
    
    bmi = state['bmi']
    label = ''
    if bmi > 30:

        state['label'] = "obese"
   
    elif bmi<=30 and bmi >=25 :
        
        state['label'] = "overweight"
    elif bmi>=18.5 and bmi<25:
        state['label'] = "normal"
    
    else:
        state['label'] = "underweight"


    return state
12/17:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
12/18:
# define State
class BMIState(TypedDict):

    weight_kg:float
    height_m: float
    bmi:float
    label: str
12/19:
def calculate_bmi(state : BMIState) -> BMIState :

    weight = state['weight_kg']
    height = state['height_m']
    
    bmi = weight/(height**2)
    state['bmi'] = round(bmi,2)

    return state
12/20:
def label_bmi(state : BMIState) -> BMIState:
    
    bmi = state['bmi']
    label = ''
    if bmi > 30:

        state['label'] = "obese"
   
    elif bmi<=30 and bmi >=25 :
        
        state['label'] = "overweight"
    elif bmi>=18.5 and bmi<25:
        state['label'] = "normal"
    
    else:
        state['label'] = "underweight"


    return state
12/21:
# define your graph
graph = StateGraph(BMIState)

# add nodes to your graph

graph.add_node('calculate_bmi', calculate_bmi)
graph.add_node('label_bmi', label_bmi)

# add edges to your graph

graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', 'label_bmi')
graph.add_edge('label_bmi', END)



# compile the graph

workflow = graph.compile()
12/22:

# execute the graph

initial_state = {'weight_kg':80, 'height_m': 1.73} 
final_state = workflow.invoke(initial_state)
print(final_state)
12/23:

# execute the graph

initial_state = {'weight_kg':80, 'height_m': 1.73} 
final_state = workflow.invoke(initial_state)
print(final_state)
12/24:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
13/1: from langgraph.graph import Stategraph
13/2: from langgraph.graph import Stategraph
13/3: from langgraph.graph import StateGraph
13/4:
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
13/5: load_dotenv()
13/6: model = ChatOpenAI()
13/7:
class LLMState(TypedDict):
    question: str
    answere: str
13/8:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
13/9:
# create graph

graph = StateGraph(LLMState)

graph.add_node('llm_qa',llm_qa)

graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

workflow = graph.compile()
13/10:
def llm_qa(state: LLMState) -> LLMState:
    
    return state
13/11:
# create graph

graph = StateGraph(LLMState)

graph.add_node('llm_qa',llm_qa)

graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

workflow = graph.compile()
13/12:
initial_state = {}
final_state = workflow.invoke(initial_state)
13/13:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png)
13/14:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
13/15:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    # update the answer in the state


    return state
13/16:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answere'] = answer


    return state
13/17:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
13/18:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/19:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/20:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
13/21: load_dotenv()
13/22: model = ChatOpenAI()
13/23:
class LLMState(TypedDict):
    question: str
    answere: str
13/24:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answere'] = answer


    return state
13/25:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
13/26:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/27: load_dotenv()
13/28:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/29:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
13/30:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
13/31: model = ChatGroq()
13/32:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
13/33:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
13/34:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
13/35:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)
13/36:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/37:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192-tool-use-preview"
)
13/38:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/39:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)
13/40:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
13/41:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)
13/42:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
14/1:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
14/2:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
14/3: load_dotenv()
14/4:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)
14/5:
class LLMState(TypedDict):
    question: str
    answere: str
14/6:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answere'] = answer


    return state
14/7:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
14/8:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
14/9: load_dotenv()
14/10:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)
14/11:
class LLMState(TypedDict):
    question: str
    answere: str
14/12:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answere'] = answer


    return state
14/13:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
14/14:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
17/1:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768"
)
17/2:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
17/3: load_dotenv()
17/4:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
17/5: load_dotenv()
17/6:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768"
)
17/7:
class LLMState(TypedDict):
    question: str
    answere: str
17/8:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answere'] = answer


    return state
17/9:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
17/10:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
17/11:
class LLMState(TypedDict):
    question: str
    answer: str
17/12:
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv
import os
17/13: load_dotenv()
17/14:
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768"
)
17/15:
class LLMState(TypedDict):
    question: str
    answer: str
17/16:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
17/17:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
17/18:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
18/1:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
18/2: load_dotenv()
18/3:
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)
18/4:
class LLMState(TypedDict):
    question: str
    answer: str
18/5:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
18/6:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
18/7:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
18/8:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
18/9: load_dotenv()
18/10:
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)
18/11:
class LLMState(TypedDict):
    question: str
    answer: str
18/12:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
18/13:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
18/14:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
19/1:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
19/2: load_dotenv()
19/3:
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)
19/4:
class LLMState(TypedDict):
    question: str
    answer: str
19/5:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
19/6:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
19/7:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
19/8:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
19/9: load_dotenv()
19/10:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
19/11:
class LLMState(TypedDict):
    question: str
    answer: str
19/12:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
19/13:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
19/14:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
19/15:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
19/16:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
import os
19/17: load_dotenv()
19/18:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
19/19:
class LLMState(TypedDict):
    question: str
    answer: str
19/20:
def llm_qa(state: LLMState) -> LLMState:
    
    # extract the question from state
    question = state['question']

    # form a prompt 
    prompt = f"""
            Answer the following question
            {question}"""

    # ask that question from llm_qa

    answer = model.invoke(prompt).content

    # update the answer in the state

    state['answer'] = answer


    return state
19/21:
# create graph

graph = StateGraph(LLMState)

# add node to graph
graph.add_node('llm_qa',llm_qa)

# add edge to graph
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

# compile graph
workflow = graph.compile()
19/22:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
19/23:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
19/24:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
print(final_state)
19/25:
#execute
initial_state = {'question': 'How far is moon from earth'}
final_state = workflow.invoke(initial_state)
print(final_state['answer'])
20/1: from langgraph.graph import StateGraph
20/2:
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
20/3: load_dotenv()
20/4:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
20/5:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
20/6:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
20/7:
def generate_outline(state : PromptState) -> PromptState:

    return state
20/8:
def generate_blog(state: PromptState) -> PromptState:

    return state
20/9:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state)
20/10:
from IPython import Image
Image(workflow.get_graph().draw_mermaid_png())
20/11:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
20/12:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
20/13: load_dotenv()
20/14:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
20/15:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
20/16:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
20/17:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
20/18:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')

workflow = graph.compile()
20/19:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state)
20/20:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
20/21:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['outline'])
20/22:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluate: int
20/23:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluate: int
20/24:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluate: int
20/25:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: int
20/26:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
20/27: load_dotenv()
20/28:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
20/29:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: int
20/30:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
20/31:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
20/32:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluate'] = evalauate_value
    return state
20/33:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
20/34:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
20/35:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
20/36: load_dotenv()
20/37:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
20/38:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: int
20/39:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
20/40:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
20/41:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluate'] = evalauate_value
    return state
20/42:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
20/43:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state)
20/44:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
20/45:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
22/1:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
22/2: load_dotenv()
22/3:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
22/4:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
22/5:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
22/6:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
22/7:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluate'] = evalauate_value
    return state
22/8:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
22/9:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
22/10:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
22/11: load_dotenv()
22/12:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
22/13:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
22/14:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
22/15:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
22/16:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
22/17:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
22/18:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
22/19:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
22/20:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
22/21: load_dotenv()
22/22:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
22/23:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
22/24:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
22/25:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
22/26:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
22/27:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
22/28:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
22/29:
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
22/30: load_dotenv()
22/31:
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
22/32:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
22/33:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
22/34:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
22/35:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
22/36:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
22/37:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
26/1:
from langgraph.graph import StateGraph
from
26/2:
from langgraph.graph import StateGraph
from typing import TypedDic
26/3: from langgraph.graph import StateGraph
27/1:
from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
27/2: load_dotenv()
27/3: load_dotenv()
27/4:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallPerBoundary: int
    summary: str
27/5:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/6:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_edge('summaryNode', generateSummary)
27/7:
def calculateSR(state: BatsmanState) -> BatsmanState:


    retunr state
27/8:
def calculateSR(state: BatsmanState) -> BatsmanState:


    return state
27/9:
def calculateBP(state: BatsmanState) -> BatsmanState:


    return state
27/10:
def calculateBPB(state: BatsmanState) -> BatsmanState:


    return state
27/11:
def generateSummary(state: BatsmanState) -> BatsmanState:


    return state
27/12:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_edge('summaryNode', generateSummary)
27/13:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_edge('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/14:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/15:
from IPython.display Image
Image(workflow.get_graph().draw_mermaid_png())
27/16:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/17:
def calculateSR(state: BatsmanState) -> BatsmanState:
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    state['strikeRate'] = strikeRate

    return state
27/18:
def calculateBP(state: BatsmanState) -> BatsmanState:
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    state['boundryPercent']= boundryPercentage
    return state
27/19:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BoundaryPerBall: int
    summary: str
27/20:
def calculateBPB(state: BatsmanState) -> BatsmanState:
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(totalBoundries/balls, 2)

    state['BoundaryPerBall']= boundryPerBall
    return state
27/21:
initial_state= {'runs': 120, 'balls': 40, 'fours': 10, 'sixes': 6}
final_state = workflow.invoke(initial_state)

print(final_state)
27/22:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/23:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/24:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {state['BallsPerBoundry']: boundryPerBall}
27/25:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/26: load_dotenv()
27/27:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/28:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/29:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': boundryPercentage}
27/30:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {state['BallsPerBoundry']: boundryPerBall}
27/31:
def generateSummary(state: BatsmanState) -> BatsmanState:


    return state
27/32:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/33:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/34:
initial_state= {'runs': 120, 'balls': 40, 'fours': 10, 'sixes': 6}
final_state = workflow.invoke(initial_state)

print(final_state)
27/35:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/36: load_dotenv()
27/37:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/38:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/39:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': boundryPercentage}
27/40:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/41:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/42:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/43:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/44:
initial_state= {'runs': 120, 'balls': 40, 'fours': 10, 'sixes': 6}
final_state = workflow.invoke(initial_state)

print(final_state)
27/45:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/46: load_dotenv()
27/47:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/48:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/49:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2}
27/50:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/51: load_dotenv()
27/52:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/53:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/54:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/55:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/56:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/57:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/58:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/59:
initial_state= {'runs': 120, 'balls': 40, 'fours': 10, 'sixes': 6}
final_state = workflow.invoke(initial_state)

print(final_state)
27/60:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/61: load_dotenv()
27/62:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/63:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/64:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/65:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/66:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/67:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/68:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/69:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
27/70:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/71: load_dotenv()
27/72:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/73:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/74:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/75:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/76:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary11':summary}
27/77:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/78:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/79:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
27/80:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/81: load_dotenv()
27/82:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/83:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/84:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/85:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry1': boundryPerBall}
27/86:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary11':summary}
27/87:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/88:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/89:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
27/90:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/91: load_dotenv()
27/92:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/93:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/94:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/95:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/96:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/97:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/98:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/99:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
27/100:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/101: load_dotenv()
27/102:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/103:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/104:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/105:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/106:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/107:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/108:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/109:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
27/110:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
27/111: load_dotenv()
27/112:
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    strikeRate: float
    boundryPercent: float
    BallsPerBoundry: int
    summary: str
27/113:
def calculateSR(state: BatsmanState):
    runs = state['runs']
    balls = state['balls']
    
    strikeRate = runs/balls*100
    

    return {'strikeRate': strikeRate}
27/114:
def calculateBP(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    runs= state['runs']

    boundries = (4*fours)+(6*sixes)
    boundryPercentage= boundries/runs*100
    
    return {'boundryPercent': round(boundryPercentage, 2)}
27/115:
def calculateBPB(state: BatsmanState):
    fours= state['fours']
    sixes= state['sixes']
    balls= state['balls']

    totalBoundries= fours + sixes
    boundryPerBall= round(balls/totalBoundries, 2)

    
    return {'BallsPerBoundry': boundryPerBall}
27/116:
def generateSummary(state: BatsmanState):
    summary= "hello"

    return {'summary':summary}
27/117:
graph = StateGraph(BatsmanState)

graph.add_node('strikeRateNode', calculateSR)
graph.add_node('boundryPercentNode', calculateBP)
graph.add_node('BoundryPerBallNode', calculateBPB)
graph.add_node('summaryNode', generateSummary)

graph.add_edge(START, 'strikeRateNode')
graph.add_edge(START, 'boundryPercentNode')
graph.add_edge(START, 'BoundryPerBallNode')

graph.add_edge('strikeRateNode', 'summaryNode')
graph.add_edge('boundryPercentNode', 'summaryNode')
graph.add_edge('BoundryPerBallNode', 'summaryNode')
graph.add_edge('summaryNode', END)

workflow = graph.compile()
27/118:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
27/119:
initial_state= {
    'runs': 120, 
    'balls': 40, 
    'fours': 10, 
    'sixes': 6
    }
final_state = workflow.invoke(initial_state)

print(final_state)
28/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
28/2:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
28/3: load_dotenv()
28/4:
model = HuggingFaceEndpoint(
    model="moonshotai/Kimi-K2-Thinking:novita"
)
28/5:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
28/6:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
28/7:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
28/8:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
28/9:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
28/10:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
28/11:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
import os
28/12: load_dotenv()
28/13:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

# Initialize Hugging Face model
model = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    huggingface_api_key=HF_API_KEY,
    temperature=0.7,
    max_new_tokens=512
)
28/14:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
28/15:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
28/16:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
28/17:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
28/18:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
28/19:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
29/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
import os
29/2: load_dotenv()
29/3:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

# Initialize Hugging Face model
model = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    huggingface_api_key=HF_API_KEY,
    temperature=0.7,
    max_new_tokens=512
)
29/4:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
29/5:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
29/6:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
29/7:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
29/8:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
29/9:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
29/10:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
import os
29/11: load_dotenv()
29/12:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="moonshotai/Kimi-K2-Thinking",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
30/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from typing import TypedDict
from dotenv import load_dotenv
import os
30/2: load_dotenv()
30/3:
# Read key from .env
from huggingface_hub import InferenceClient


HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="moonshotai/Kimi-K2-Thinking",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/2: load_dotenv()
31/3:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

# Create HF client
client = InferenceClient(
    model="moonshotai/Kimi-K2-Thinking",
    token=HF_API_KEY
)

# HuggingFaceEndpoint STILL needs repo_id
model = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/4:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/5:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
31/6:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
31/7:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/8:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/9:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/10:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/11: load_dotenv()
31/12:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

# Create HF client
client = InferenceClient(
    model="moonshotai/Kimi-K2-Thinking:novita",
    token=HF_API_KEY
)

# HuggingFaceEndpoint STILL needs repo_id
model = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking:novita",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/13:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/14:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
31/15:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
31/16:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/17:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/18:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/19:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/20: load_dotenv()
31/21:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/22:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/23:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
31/24:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
31/25:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/26:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/27:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/28:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/29: load_dotenv()
31/30:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/31:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/32:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt).content

    # update state

    state['outline'] = outline


    return state
31/33:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
31/34:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/35:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/36:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/37:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/38: load_dotenv()
31/39:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/40:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/41:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/42:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt).content
    state['content'] = content
    return state
31/43:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/44:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/45:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/46:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/47: load_dotenv()
31/48:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/49:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/50:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/51:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/52:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt).content
    state['evaluator'] = evalauate_value
    return state
31/53:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/54:
initial_state = {'topic': "Beautiful World"}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/55:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/56: load_dotenv()
31/57:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/58:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/59:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/60:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/61:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    
    evalauate_value = model.invoke(prompt)
    state['evaluator'] = evalauate_value
    return state
31/62:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/63:
initial_state = {
    "topic": "Beautiful World",
    "outline": "",
    "content": "",
    "evaluator": ""
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/64:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/65: load_dotenv()
31/66:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/67:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/68:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/69:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/70:
def evalaute(state: PromptState) -> PromptState:
    topic = state['topic']
    outline = state['outline']
    content = state['content']
    
    prompt = f"""
            Evaluate blog{content} and provide rating from 1 to 5. 
            Respond ONLY with a single integer. No explanation
            """
    evalauate_value = str(model.invoke(prompt)).strip()
    state['evaluator'] = evalauate_value

    return state
31/71:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/72:
initial_state = {
    "topic": "Beautiful World",
    "outline": "",
    "content": "",
    "evaluator": ""
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/73:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/74: load_dotenv()
31/75:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/76:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/77:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/78:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/79:
def evalaute(state: PromptState) -> PromptState:
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    return state
31/80:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/81:
initial_state = {
    "topic": "Beautiful World",
    "outline": "",
    "content": "",
    "evaluator": ""
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/82:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/83: load_dotenv()
31/84:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/85:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/86:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/87:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/88:
def evalaute(state: PromptState) -> PromptState:
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    return state
31/89:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/90:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
31/91:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
31/92: load_dotenv()
31/93:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
31/94:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
31/95:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
31/96:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
31/97:
def evalaute(state: PromptState) -> PromptState:
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    return state
31/98:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
31/99:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/2: load_dotenv()
32/3:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
32/4:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/5:
def generate_outline(state : PromptState) -> PromptState:

    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state

    state['outline'] = outline


    return state
32/6:
def generate_blog(state: PromptState) -> PromptState:

    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    state['content'] = content
    return state
32/7:
def evalaute(state: PromptState) -> PromptState:
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    return state
32/8:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/9:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/10:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/11: load_dotenv()
32/12:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
32/13:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/14:
def generate_outline(state : PromptState) -> PromptState:
    print(">> generate_outline state in:", state)
    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state
    print(">> generate_outline state out:", state)
    state['outline'] = outline


    return state
32/15:
def generate_blog(state: PromptState) -> PromptState:
    print(">> generate_blog state in:", state)
    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    
    state['content'] = content
    print(">> generate_blog state out:", state)
    return state
32/16:
def evalaute(state: PromptState) -> PromptState:
    print(">> evaluate state in:", state)
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    print(">> evaluate state out:", state)
    return state
32/17:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/18:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/19:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/20: load_dotenv()
32/21:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=HF_API_KEY
)

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    client=client,
    temperature=0.7,
    max_new_tokens=512
)
32/22:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/23:
def generate_outline(state : PromptState) -> PromptState:
    print(">> generate_outline state in:", state)
    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state
    print(">> generate_outline state out:", state)
    state['outline'] = outline


    return state
32/24:
def generate_blog(state: PromptState) -> PromptState:
    print(">> generate_blog state in:", state)
    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    
    state['content'] = content
    print(">> generate_blog state out:", state)
    return state
32/25:
def evalaute(state: PromptState) -> PromptState:
    print(">> evaluate state in:", state)
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    print(">> evaluate state out:", state)
    return state
32/26:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/27:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/28:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/29: load_dotenv()
32/30:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)
32/31:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/32:
def generate_outline(state : PromptState) -> PromptState:
    print(">> generate_outline state in:", state)
    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state
    print(">> generate_outline state out:", state)
    state['outline'] = outline


    return state
32/33:
def generate_blog(state: PromptState) -> PromptState:
    print(">> generate_blog state in:", state)
    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    
    state['content'] = content
    print(">> generate_blog state out:", state)
    return state
32/34:
def evalaute(state: PromptState) -> PromptState:
    print(">> evaluate state in:", state)
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    print(">> evaluate state out:", state)
    return state
32/35:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/36:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/37:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/38: load_dotenv()
32/39:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)
32/40:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/41:
def generate_outline(state : PromptState) -> PromptState:
    print(">> generate_outline state in:", state)
    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state
    print(">> generate_outline state out:", state)
    state['outline'] = outline


    return state
32/42:
def generate_blog(state: PromptState) -> PromptState:
    print(">> generate_blog state in:", state)
    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    
    state['content'] = content
    print(">> generate_blog state out:", state)
    return state
32/43:
def evalaute(state: PromptState) -> PromptState:
    print(">> evaluate state in:", state)
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    print(">> evaluate state out:", state)
    return state
32/44:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/45:
initial_state = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None
}
final_state = workflow.invoke(initial_state)

print(final_state['evaluator'])
32/46:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
32/47: load_dotenv()
32/48:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)
32/49:
class PromptState(TypedDict):
    topic: str
    outline: str
    content: str
    evaluator: str
32/50:
def generate_outline(state : PromptState) -> PromptState:
    print(">> generate_outline state in:", state)
    # fetch title/topic
    topic = state['topic']

    # call llm
    prompt = f"""
            create a detailed outline for following topic
            {topic}
            """
    
    outline = model.invoke(prompt)

    # update state
    print(">> generate_outline state out:", state)
    state['outline'] = outline


    return state
32/51:
def generate_blog(state: PromptState) -> PromptState:
    print(">> generate_blog state in:", state)
    topic = state['topic']
    outline = state['outline']
    
    prompt = f"""
            create a blog for following topic
            {topic} and use detailed outline {outline}
            """
    
    content = model.invoke(prompt)
    
    state['content'] = content
    print(">> generate_blog state out:", state)
    return state
32/52:
def evalaute(state: PromptState) -> PromptState:
    print(">> evaluate state in:", state)
    content = state['content']
    
    prompt = f"""
Evaluate the following blog:

{content}

Provide a rating from 1 to 5.
Respond ONLY with a single integer.
"""
    
    result = model.invoke(prompt)
    state['evaluator'] = str(result).strip()
    print(">> evaluate state out:", state)
    return state
32/53:
graph = StateGraph(PromptState)

graph.add_node('generate_outline', generate_outline)
graph.add_node('generate_blog', generate_blog)
graph.add_node('evaluate', evalaute)

graph.add_edge(START, 'generate_outline')
graph.add_edge('generate_outline', 'generate_blog')
graph.add_edge('generate_blog', 'evaluate')
graph.add_edge('evaluate', END)
workflow = graph.compile()
32/54:
state: PromptState = {
    "topic": "Beautiful World",
    "outline": None,
    "content": None,
    "evaluator": None,
}

print(">>> calling generate_outline")
state = generate_outline(state)
print("outline:\n", state["outline"], "\n")

print(">>> calling generate_blog")
state = generate_blog(state)
print("content:\n", state["content"], "\n")

print(">>> calling evalaute")
state = evalaute(state)
print("evaluator:\n", state["evaluator"])
32/55:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))
32/56:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
32/57:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/58:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/59:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    provider="hf-inference",   # ← FORCE real HF API
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/60:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_API_KEY,
    task="conversational",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/61:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.7,
    max_new_tokens=200
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/62:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")


model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_API_KEY,
    task="conversational",
    temperature=0.7,
    max_new_tokens=512,
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/63:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

os.environ["HUGGINGFACEHUB_API_TOKEN"] =HF_API_KEY

model = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    temperature=0.7,
    max_new_tokens=200
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/64:
# Read key from .env
HF_API_KEY = os.getenv("HF_API_KEY")

os.environ["HUGGINGFACEHUB_API_TOKEN"] =HF_API_KEY
if "HF_ENDPOINT" in os.environ:
    del os.environ["HF_ENDPOINT"]
os.environ["HF_ENDPOINT"] = "https://api-inference.huggingface.co"

model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation",   # IMPORTANT
    max_new_tokens=100
)

print("HF_API_KEY:", HF_API_KEY)

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Model output:", out)
except Exception as e:
    print("Actual HF error:", repr(e))

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("REAL ERROR:", repr(e))
import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

resp = requests.post(url, json={"inputs": "hello"}, headers=headers)
print(resp.status_code, resp.text)
32/65:
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="google/flan-t5-large",
    token="hf_your_api_key"
)

response = client.text_generation("Explain LangGraph simply")
print(response)
32/66:
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(
    model="google/flan-t5-large",
    token="hf_your_api_key"
)

response = client.text_generation("Explain LangGraph simply")
print(response)
33/1:
from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import HuggingFaceEndpoint
from huggingface_hub import InferenceClient
from typing import TypedDict
from dotenv import load_dotenv
import os
33/2: load_dotenv()
33/3:
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(
    model="google/flan-t5-large",
    token="hf_your_api_key"
)

response = client.text_generation("Explain LangGraph simply")
print(response)
33/4:
import os
from langchain_community.llms import HuggingFaceEndpoint

# Load API key
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("HF_API_KEY is missing from environment")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_API_KEY

# IMPORTANT: do NOT set HF_ENDPOINT
if "HF_ENDPOINT" in os.environ:
    del os.environ["HF_ENDPOINT"]

# Model
model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation",
    max_new_tokens=100
)

print("HF_API_KEY loaded:", HF_API_KEY[:6] + "...")

try:
    print("Calling HF model...")
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("ERROR:", repr(e))
33/5:
import os
from langchain_huggingface import HuggingFaceEndpoint

HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("HF_API_KEY missing")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_API_KEY

# DO NOT set HF_ENDPOINT
if "HF_ENDPOINT" in os.environ:
    del os.environ["HF_ENDPOINT"]

model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation",
    max_new_tokens=100
)

print("Calling HF model...")

try:
    out = model.invoke("Say hello in one short sentence.")
    print("Output:", out)
except Exception as e:
    print("ERROR:", repr(e))
34/1:
from langgraph import Stategraph
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
34/2:
from langgraph import StateGraph
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
34/3:
from langgraph import StateGraph
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
34/4:
from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
34/5: load_dotenv()
34/6:
class EssayState(TypedDict):
    essay: str
    topic: str
    clarityOfThought: int
    DepthOfAnalysis: int
    Language: int
34/7: def calculateClarityOfThoughts(state: EssayState):
34/8:
def calculateClarityOfThoughts(state: EssayState):
    
    return "helo"
34/9:
def calculateDOA(state: EssayState):
    
    return "hello"
34/10:
def calculateLanguage(state: EssayState):
    
    return "Hello"
34/11:
graph = StateGraph(EssayState)

graph.add_node("clarityOfThoughtsNode", calculateClarityOfThoughts)
graph.add_node("DOANode", calculateDOA)
graph.add_node("LanguageNode", calculateLanguage)
graph.add_node("finalEvaluationNode", calculateFinalEvaluation)

graph.add_edge(START, "clarityOfThoughtsNode")
graph.add_edge(START, "DOANode")
graph.add_edge(START, "LanguageNode")
graph.add_edge('clarityOfThoughtsNode', 'finalEvaluationNode')
graph.add_edge('DOANode', 'finalEvaluationNode')
graph.add_edge('LanguageNode', 'finalEvaluationNode')
graph.add_edge('finalEvaluationNode', END)


workflow= graph.compile()
34/12:
def calculateFinalEvaluation(state: EssayState):
    return "hello"
34/13:
graph = StateGraph(EssayState)

graph.add_node("clarityOfThoughtsNode", calculateClarityOfThoughts)
graph.add_node("DOANode", calculateDOA)
graph.add_node("LanguageNode", calculateLanguage)
graph.add_node("finalEvaluationNode", calculateFinalEvaluation)

graph.add_edge(START, "clarityOfThoughtsNode")
graph.add_edge(START, "DOANode")
graph.add_edge(START, "LanguageNode")
graph.add_edge('clarityOfThoughtsNode', 'finalEvaluationNode')
graph.add_edge('DOANode', 'finalEvaluationNode')
graph.add_edge('LanguageNode', 'finalEvaluationNode')
graph.add_edge('finalEvaluationNode', END)


workflow= graph.compile()
34/14:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
34/15: load_dotenv()
34/16:
graph = StateGraph(EssayState)

graph.add_node("clarityOfThoughtsNode", calculateClarityOfThoughts)
graph.add_node("DOANode", calculateDOA)
graph.add_node("LanguageNode", calculateLanguage)
graph.add_node("finalEvaluationNode", calculateFinalEvaluation)

graph.add_edge(START, "clarityOfThoughtsNode")
graph.add_edge(START, "DOANode")
graph.add_edge(START, "LanguageNode")
graph.add_edge('clarityOfThoughtsNode', 'finalEvaluationNode')
graph.add_edge('DOANode', 'finalEvaluationNode')
graph.add_edge('LanguageNode', 'finalEvaluationNode')
graph.add_edge('finalEvaluationNode', END)


workflow= graph.compile()
34/17:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
34/18:
def calculateClarityOfThoughts(state: EssayState):
    topic= state["topic"]
    essay= state["essay"]

    prompt= f"""
            Provide an integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            and topic is
            {topic}

    clarityOfThought = model.invoke(prompt).content
34/19:
def calculateClarityOfThoughts(state: EssayState):
    topic= state["topic"]
    essay= state["essay"]

    prompt= f"""
            Provide an integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            and topic is
            {topic}
            """

    clarityOfThought = model.invoke(prompt).content
34/20: model = ChatOpenAI(model= 'gpt-4o-mini')
34/21:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
34/22: load_dotenv()
34/23: model = ChatOpenAI(model= 'gpt-4o-mini')
34/24:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10', ge=0, gt=10)
34/25: structured_model = model.with_structured_output(EssaySchema)
34/26:
essay= """"
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
34/27:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {essay}
"""
34/28:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {essay}
"""
structured_model.invoke(prompt)
34/29: load_dotenv()
34/30: model = ChatOpenAI(model= 'gpt-4o-mini')
34/31:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {essay}
"""
structured_model.invoke(prompt)
35/1:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
35/2: load_dotenv()
35/3: model = ChatOpenAI(model= 'gpt-4o-mini')
35/4:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10', ge=0, gt=10)
35/5: structured_model = model.with_structured_output(EssaySchema)
35/6:
essay= """"
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/7:
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
35/8:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
35/9:
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
35/10: model = ChatOpenAI(model= 'gpt-4o-mini')
35/11:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10', ge=0, gt=10)
35/12: structured_model = model.with_structured_output(EssaySchema)
35/13:
essay= """"
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/14:
model = ChatOpenAI(
    model= 'gpt-4o-mini'
    api_key=os.getenv("OPENAI_API_KEY")
    )
35/15:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
    )
35/16:
essay= """
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/17:
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
35/18:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
    )
35/19:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10', ge=0, gt=10)
35/20: structured_model = model.with_structured_output(EssaySchema)
35/21:
essay= """
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/22:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {essay}
"""
structured_model.invoke(prompt)
35/23:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10', ge=0, le=10)
35/24:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {essay}
"""
structured_model.invoke(prompt)
35/25:
prompt= f"""
Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10:
{essay}
"""
structured_model.invoke(prompt)
35/26:
prompt = f"""
Evaluate the following essay and return ONLY a JSON object with exactly these fields:
- feedback: string
- score: integer from 0 to 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt)
print(result)
35/27: structured_model = model.with_structured_output(EssaySchema, strict=True)
35/28:
prompt = f"""
Evaluate the following essay and return ONLY a JSON object with exactly these fields:
- feedback: string
- score: integer from 0 to 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt)
print(result)
35/29:
prompt = f"""
Evaluate the following essay and return ONLY a JSON object with exactly these fields:
- feedback: string
- score: integer from 0 to 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt).feedback
print(result)
35/30:
prompt = f"""
Evaluate the following essay and return ONLY a JSON object with exactly these fields:
- feedback: string
- score: integer from 0 to 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt).score
print(result)
35/31:
prompt = f"""
Evaluate the  langauge quality of the following essay. Provide a detailed feedback and score out of 10/

Essay:
{essay}
"""

result = structured_model.invoke(prompt).score
print(result)
35/32:
prompt = f"""
Evaluate the  langauge quality of the following essay. Provide a detailed feedback and score out of 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt).score
print(result)
35/33:
def calculateClarityOfThoughts(state: EssayState):
    topic= state["topic"]
    essay= state["essay"]

    prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

    clarityOfThought = structured_model.invoke(prompt).feedback
    print(clarityOfThought)
35/34:
class EssayState(TypedDict):
    essay: str 
    clarityOfThought_feedback: str
    DepthOfAnalysis_feedback: str
    Language_feedback: str
    summary_feedback: str
    avg_final_score: float
    individual_score: list[int]
35/35:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

    clarityOfThought = structured_model.invoke(prompt).feedback
    print(clarityOfThought)
35/36:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

    clarityOfThought = structured_model.invoke(prompt).feedback
    print(clarityOfThought)
35/37:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

    clarityOfThought = structured_model.invoke(prompt).feedback
    print(clarityOfThought)
35/38:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

    clarityOfThought = structured_model.invoke(prompt)
    print(clarityOfThought)
35/39:
prompt= f"""
            Provide a detailed feedback and integer ratings from 1- 10. Rate on the basis of clarity of thoughts for following essay:
            {essay}
            """

clarityOfThought = structured_model.invoke(prompt)
print(clarityOfThought)
35/40:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
import operator
35/41:
class EssayState(TypedDict):
    essay: str 
    clarityOfThought_feedback: str
    DepthOfAnalysis_feedback: str
    Language_feedback: str
    summary_feedback: str
    avg_final_score: float
    individual_score: Annotated[list[int], operator.add]
35/42:
class EssayState(TypedDict):
    essay: str 
    clarityOfThought_feedback: str
    DepthOfAnalysis_feedback: str
    Language_feedback: str
    summary_feedback: str
    avg_final_score: float
    individual_score: Annotated[list[int], operator.add]
35/43:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
import operator
35/44:
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
35/45:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
    )
35/46:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10 only', ge=0, le=10)
35/47: structured_model = model.with_structured_output(EssaySchema, strict=True)
35/48:
essay= """
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/49:
prompt = f"""
Evaluate the  langauge quality of the following essay. Provide a detailed feedback and score out of 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt).score
print(result)
35/50:
class EssayState(TypedDict):
    essay: str 
    clarityOfThought_feedback: str
    DepthOfAnalysis_feedback: str
    Language_feedback: str
    summary_feedback: str
    avg_final_score: float
    individual_score: Annotated[list[int], operator.add]
35/51:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed clarity of thoughts feedback and integer ratings from 1- 10 for following essay:
            {state['essay']}
            """

    clarityOfThought = structured_model.invoke(prompt)
    return {'clarityOfThought_feedback': clarityOfThought.feedback, 'individual_score':[clarityOfThought.score]}
35/52:
def calculateDOA(state: EssayState):
    
        
    prompt = f"""
    Evaluate the depth of analysis quality of following essay and return ONLY a JSON object with exactly these fields:
    - feedback: string
    - score: integer from 0 to 10

    Essay:
    {state['essay']}
    """

    result = structured_model.invoke(prompt)
    return {'DepthOfAnalysis_feedback': result.feedback, 'individual_score': [result.score]}
35/53:
def calculateLanguage(state: EssayState):
    
    prompt = f"""
    Evaluate the language quality of following essay and return ONLY a JSON object with exactly these fields:
    - feedback: string
    - score: integer from 0 to 10

    Essay:
    {state['essay']}
    """

    result = structured_model.invoke(prompt)
    return {'Language_feedback': result.feedback, 'individual_score': [result.score]}
35/54:
def calculateFinalEvaluation(state: EssayState):
    prompt = f"""
    Provide a summerised overall feedback based on following feedbacks:
    language feedback {state['Language_feedback']},
    clarity Of Thought feedback {state['clarityOfThought_feedback']}
    depth of analysis feedback{state['DepthOfAnalysis_feedback']}
    """

    result = model.invoke(prompt)

    average_score= sum(state['individual_score'])/len(state['individual_score'])
    return {'summary_feedback': result,'avg_final_score' : average_score}
35/55:
graph = StateGraph(EssayState)

graph.add_node("clarityOfThoughtsNode", calculateClarityOfThoughts)
graph.add_node("DOANode", calculateDOA)
graph.add_node("LanguageNode", calculateLanguage)
graph.add_node("finalEvaluationNode", calculateFinalEvaluation)

graph.add_edge(START, "clarityOfThoughtsNode")
graph.add_edge(START, "DOANode")
graph.add_edge(START, "LanguageNode")
graph.add_edge('clarityOfThoughtsNode', 'finalEvaluationNode')
graph.add_edge('DOANode', 'finalEvaluationNode')
graph.add_edge('LanguageNode', 'finalEvaluationNode')
graph.add_edge('finalEvaluationNode', END)


workflow= graph.compile()
35/56:
initial_state={
    essay
}
final_state=  workflow.invoke(initial_state)
print(final_state)
35/57:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
import operator
35/58:
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
35/59:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
    )
35/60:
class EssaySchema(BaseModel):
    feedback: str= Field(description='Detailed feedback for the essay')
    score: int= Field(description='Score out of 10 only', ge=0, le=10)
35/61: structured_model = model.with_structured_output(EssaySchema, strict=True)
35/62:
essay= """
The world is beautiful not because it is perfect, but because it is alive. Every sunrise paints a new beginning, and every sunset reminds us to pause. Nature’s rhythms—waves, winds, and wandering clouds—quietly teach us balance. People, too, add to this beauty through kindness, curiosity, and connection. Even in chaos, moments of hope emerge, proving that beauty often hides in the ordinary. When we choose to notice these details, the world feels larger, softer, and more meaningful. A beautiful world is not something we find; it is something we learn to see
"""
35/63:
prompt = f"""
Evaluate the  langauge quality of the following essay. Provide a detailed feedback and score out of 10

Essay:
{essay}
"""

result = structured_model.invoke(prompt).score
print(result)
35/64:
class EssayState(TypedDict):
    essay: str 
    clarityOfThought_feedback: str
    DepthOfAnalysis_feedback: str
    Language_feedback: str
    summary_feedback: str
    avg_final_score: float
    individual_score: Annotated[list[int], operator.add]
35/65:
def calculateClarityOfThoughts(state: EssayState):
    
    #essay= state["essay"]

    prompt= f"""
            Provide a detailed clarity of thoughts feedback and integer ratings from 1- 10 for following essay:
            {state['essay']}
            """

    clarityOfThought = structured_model.invoke(prompt)
    return {'clarityOfThought_feedback': clarityOfThought.feedback, 'individual_score':[clarityOfThought.score]}
35/66:
def calculateDOA(state: EssayState):
    
        
    prompt = f"""
    Evaluate the depth of analysis quality of following essay and return ONLY a JSON object with exactly these fields:
    - feedback: string
    - score: integer from 0 to 10

    Essay:
    {state['essay']}
    """

    result = structured_model.invoke(prompt)
    return {'DepthOfAnalysis_feedback': result.feedback, 'individual_score': [result.score]}
35/67:
def calculateLanguage(state: EssayState):
    
    prompt = f"""
    Evaluate the language quality of following essay and return ONLY a JSON object with exactly these fields:
    - feedback: string
    - score: integer from 0 to 10

    Essay:
    {state['essay']}
    """

    result = structured_model.invoke(prompt)
    return {'Language_feedback': result.feedback, 'individual_score': [result.score]}
35/68:
def calculateFinalEvaluation(state: EssayState):
    prompt = f"""
    Provide a summerised overall feedback based on following feedbacks:
    language feedback {state['Language_feedback']},
    clarity Of Thought feedback {state['clarityOfThought_feedback']}
    depth of analysis feedback{state['DepthOfAnalysis_feedback']}
    """

    result = model.invoke(prompt)

    average_score= sum(state['individual_score'])/len(state['individual_score'])
    return {'summary_feedback': result,'avg_final_score' : average_score}
35/69:
graph = StateGraph(EssayState)

graph.add_node("clarityOfThoughtsNode", calculateClarityOfThoughts)
graph.add_node("DOANode", calculateDOA)
graph.add_node("LanguageNode", calculateLanguage)
graph.add_node("finalEvaluationNode", calculateFinalEvaluation)

graph.add_edge(START, "clarityOfThoughtsNode")
graph.add_edge(START, "DOANode")
graph.add_edge(START, "LanguageNode")
graph.add_edge('clarityOfThoughtsNode', 'finalEvaluationNode')
graph.add_edge('DOANode', 'finalEvaluationNode')
graph.add_edge('LanguageNode', 'finalEvaluationNode')
graph.add_edge('finalEvaluationNode', END)


workflow= graph.compile()
35/70:
initial_state={
    'essay':essay
}
final_state=  workflow.invoke(initial_state)
print(final_state)
35/71:
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())
35/72:
initial_state={
    'essay':essay
}
final_state=  workflow.invoke(initial_state)
print(final_state.content)
35/73:
initial_state={
    'essay':essay
}
final_state=  workflow.invoke(initial_state)
print(final_state)
35/74:
initial_state={
    'essay':essay
}
workflow.invoke(initial_state)
#print(final_state)
36/1:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
36/2: load_dotenv
36/3: load_dotenv()
36/4:
class QuadraticState(TypedDict):
    a: int
    b: int
    c: int
    d: float
    roots: list[float]
36/5: graph = StateGraph(QuadraticState)
36/6:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/7:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/8:
def cal_equation(state: QuadraticState):
    equation = f"""
            """
36/9:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x**2 {state['b']}x + {state['c']} = 0
            """
36/10:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2 {state['b']}x + {state['c']} = 0
            """
    return {'equation': equation}
36/11:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2 {state['b']}x + {state['c']} = 0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*c)

    return {'d': disc}
36/12:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
graph.add_node('non_realRootsNode', cal_nonReal)
graph.add_node('realRootsNode', cal_real)
graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
36/13:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
#graph.add_node('non_realRootsNode', cal_nonReal)
#graph.add_node('realRootsNode', cal_real)
#graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
36/14:
workflow= graph.compile()
wrokflow
36/15:
workflow= graph.compile()
workflow
36/16:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
36/17:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/18:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
#graph.add_node('non_realRootsNode', cal_nonReal)
#graph.add_node('realRootsNode', cal_real)
#graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_edge('discriminantNode', END)
36/19:
workflow= graph.compile()
workflow
36/20:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/21:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/22:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/23:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2 {state['b']}x + {state['c']} = 0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}
36/24:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/25:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from dotenv import load_dotenv
36/26: load_dotenv()
36/27:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/28:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2 {state['b']}x + {state['c']} = 0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}
36/29:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
#graph.add_node('non_realRootsNode', cal_nonReal)
#graph.add_node('realRootsNode', cal_real)
#graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_edge('discriminantNode', END)
36/30:
workflow= graph.compile()
workflow
36/31:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/32:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from dotenv import load_dotenv
36/33: load_dotenv()
36/34:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/35:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2{state['b']}x+{state['c']}=0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}
36/36:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
#graph.add_node('non_realRootsNode', cal_nonReal)
#graph.add_node('realRootsNode', cal_real)
#graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_edge('discriminantNode', END)
36/37:
workflow= graph.compile()
workflow
36/38:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/39:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from dotenv import load_dotenv
36/40: load_dotenv()
36/41:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/42:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2+{state['b']}x+{state['c']}=0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}
36/43:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
#graph.add_node('non_realRootsNode', cal_nonReal)
#graph.add_node('realRootsNode', cal_real)
#graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_edge('discriminantNode', END)
36/44:
workflow= graph.compile()
workflow
36/45:
initial_state = {
    'a':2,
    'b':3,
    'c': 6
}
workflow.invoke(initial_state)
36/46:
initial_state = {
    'a':2,
    'b':3,
    'c': 2
}
workflow.invoke(initial_state)
36/47:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2+{state['b']}x+{state['c']}=0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}

def cal_real(state: QuadraticState):

    root1= (-state['b']+state['d'])/(2*state['a'])
    root2= (-state['b']-state['d'])/(2*state['a'])
    roots= f"""
        The real roots are {root1} and {root2}
        """
    return {'roots': roots}
def cal_nonReal(state: QuadraticState):

    roots= f"""
        No real roots.
        """
    return {'roots': roots}
def cal_realRepeated(state: QuadraticState):

    root1= (-state['b'])/(2*state['a'])
    roots= f"""
        The real and repeated root is {root1}
        """
    return {'roots': roots}
36/48:
def check_condition(state: QuadraticState)-> Literal['non_realRootsNode', 'realRootsNode', 'realRootsRepeatedNode']:
    
    if state['d']> 0:
        return 'realRootsNode'
    elif state['d'] == 0:
        return 'realRootsRepeatedNode'
    else
        return 'non_realRootsNode'
36/49:
def check_condition(state: QuadraticState)-> Literal['non_realRootsNode', 'realRootsNode', 'realRootsRepeatedNode']:
    
    if state['d']> 0:
        return 'realRootsNode'
    elif state['d'] == 0:
        return 'realRootsRepeatedNode'
    else:
        return 'non_realRootsNode'
36/50:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
graph.add_node('non_realRootsNode', cal_nonReal)
graph.add_node('realRootsNode', cal_real)
graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_conditional_edges('discriminantNode', check_condition)

graph.add_edge('non_realRootsNode', END)
graph.add_edge('realRootsNode', END)
graph.add_edge('realRootsRepeatedNode', END)
36/51:
workflow= graph.compile()
workflow
36/52:
initial_state = {
    'a':2,
    'b':3,
    'c': 2
}
workflow.invoke(initial_state)
36/53:
initial_state = {
    'a':2,
    'b':1,
    'c': 1
}
workflow.invoke(initial_state)
36/54:
initial_state = {
    'a':2,
    'b':1,
    'c': 1
}
workflow.invoke(initial_state)
36/55:
initial_state = {
    'a':1,
    'b':2,
    'c': 1
}
workflow.invoke(initial_state)
36/56:
initial_state = {
    'a':4,
    'b':-5,
    'c': -4
}
workflow.invoke(initial_state)
36/57:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from dotenv import load_dotenv
36/58: load_dotenv()
36/59:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/60:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2{state['b']}x{state['c']}=0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}

def cal_real(state: QuadraticState):

    root1= (-state['b']+state['d'])/(2*state['a'])
    root2= (-state['b']-state['d'])/(2*state['a'])
    roots= f"""
        The real roots are {root1} and {root2}
        """
    return {'roots': roots}
def cal_nonReal(state: QuadraticState):

    roots= f"""
        No real roots.
        """
    return {'roots': roots}
def cal_realRepeated(state: QuadraticState):

    root1= (-state['b'])/(2*state['a'])
    roots= f"""
        The real and repeated root is {root1}
        """
    return {'roots': roots}
36/61:
def check_condition(state: QuadraticState)-> Literal['non_realRootsNode', 'realRootsNode', 'realRootsRepeatedNode']:
    
    if state['d']> 0:
        return 'realRootsNode'
    elif state['d'] == 0:
        return 'realRootsRepeatedNode'
    else:
        return 'non_realRootsNode'
36/62:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
graph.add_node('non_realRootsNode', cal_nonReal)
graph.add_node('realRootsNode', cal_real)
graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_conditional_edges('discriminantNode', check_condition)

graph.add_edge('non_realRootsNode', END)
graph.add_edge('realRootsNode', END)
graph.add_edge('realRootsRepeatedNode', END)
36/63:
workflow= graph.compile()
workflow
36/64:
initial_state = {
    'a':4,
    'b':-5,
    'c': -4
}
workflow.invoke(initial_state)
36/65:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from dotenv import load_dotenv
36/66: load_dotenv()
36/67:
class QuadraticState(TypedDict):
    
    a: int
    b: int
    c: int
    d: float
    equation: str
    roots: str
36/68:
def cal_equation(state: QuadraticState):
    equation = f"""
        {state['a']}x2{state['b']}x{state['c']}=0
            """
    return {'equation': equation}

def cal_discriminant(state: QuadraticState):

    disc = state['b']**2 - (4*state['a']*state['c'])

    return {'d': disc}

def cal_real(state: QuadraticState):

    root1= (-state['b']+(state['d'])**0.5)/(2*state['a'])
    root2= (-state['b']-(state['d'])**0.5)/(2*state['a'])
    roots= f"""
        The real roots are {root1} and {root2}
        """
    return {'roots': roots}
def cal_nonReal(state: QuadraticState):

    roots= f"""
        No real roots.
        """
    return {'roots': roots}
def cal_realRepeated(state: QuadraticState):

    root1= (-state['b'])/(2*state['a'])
    roots= f"""
        The real and repeated root is {root1}
        """
    return {'roots': roots}
36/69:
def check_condition(state: QuadraticState)-> Literal['non_realRootsNode', 'realRootsNode', 'realRootsRepeatedNode']:
    
    if state['d']> 0:
        return 'realRootsNode'
    elif state['d'] == 0:
        return 'realRootsRepeatedNode'
    else:
        return 'non_realRootsNode'
36/70:
graph = StateGraph(QuadraticState)
graph.add_node('equationNode', cal_equation)
graph.add_node('discriminantNode', cal_discriminant)
graph.add_node('non_realRootsNode', cal_nonReal)
graph.add_node('realRootsNode', cal_real)
graph.add_node('realRootsRepeatedNode', cal_realRepeated)

graph.add_edge(START, 'equationNode')
graph.add_edge('equationNode', 'discriminantNode')
graph.add_conditional_edges('discriminantNode', check_condition)

graph.add_edge('non_realRootsNode', END)
graph.add_edge('realRootsNode', END)
graph.add_edge('realRootsRepeatedNode', END)
36/71:
workflow= graph.compile()
workflow
36/72:
initial_state = {
    'a':4,
    'b':-5,
    'c': -4
}
workflow.invoke(initial_state)
36/73:
initial_state = {
    'a':4,
    'b':5,
    'c': 4
}
workflow.invoke(initial_state)
37/1:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict
37/2:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict
from dotenv import load_dotenv
37/3:
load_dotenv(
)
37/4: load_dotenv()
37/5: class CustomerSupportSchema(BaseModel):
37/6:
class CustomerSupportState(TypedDict):
    'issueType': str
    'tone': str
37/7:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/8:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/9:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
    return
37/10:
model = ChatOpenAI(
    
)
37/11:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone of the review. The tone can be positive or negative.
            - review is {review}
            """
    tone = model.invoke(prompt).content
    return {'tone': tone}
37/12:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone of the review. The tone should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    tone = model.invoke(prompt).content
    return {'tone': tone}
37/13:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone')
37/14: structured_model = model.with_structured_output(BaseModel, strict= True)
37/15: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/16:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/17:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}
37/18:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(promp).content
37/19:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)
37/20:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt).content
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt).content
     return {'response', response}
37/21:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)
37/22:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
37/23: def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']
37/24:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/25:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)

graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)
37/26:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)

graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/27:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/28:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/29: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/30:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/31:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
37/32: load_dotenv()
37/33:
model = ChatOpenAI(
    
)
37/34:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/35: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/36:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/37:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt).content
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt).content
     return {'response', response}
37/38:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/39:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/40: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/41:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/42:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
37/43: load_dotenv()
37/44:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/45:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/46: load_dotenv()
37/47:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/48:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/49: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/50:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/51:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt).content
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt).content
     return {'response', response}
37/52:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/53:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/54: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/55:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/56:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/57: prompt= f'What is the sentiment of the review - The software is too bad'
37/58:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).content
37/59:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/60: load_dotenv()
37/61:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/62:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/63: structured_model = model.with_structured_output(SentimentSchema, strict= True)
37/64:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).content
37/65:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).
37/66:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt)
37/67:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/68:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/69: load_dotenv()
37/70:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/71:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/72:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/73: structured_model = model.with_structured_output(SentimentSchema, strict= True)
37/74:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/75:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/76:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt)
     return {'response', response}
37/77:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/78:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/79: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/80:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/81: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/82:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/83: load_dotenv()
37/84:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/85:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issuetype: str = Field(description= 'Type of the issue in the review')
37/86:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/87: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/88:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/89:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/90:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt)
     return {'response', response}
37/91:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/92:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/93: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/94:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/95:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/96: load_dotenv()
37/97:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/98:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/99:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/100: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/101:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/102:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/103:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response', response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt)
     return {'response', response}
37/104:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/105:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/106: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/107:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/108:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/109: load_dotenv()
37/110:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/111:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/112:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/113: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/114:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/115:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/116:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Provide a response.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt)
     return {'response': response}
37/117:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/118:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/119: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/120:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/121:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/122: load_dotenv()
37/123:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/124:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/125:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/126: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/127:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/128:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/129:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review. Generate a response from customer support team.
        - review is {review}
        - sentiment is {sentiment}

        """
     response= structured_model.invoke(prompt)
     return {'response': response}
37/130:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/131:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/132: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/133:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/134:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/135: load_dotenv()
37/136:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/137:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/138:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/139: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/140:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/141:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/142:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review.
        - sentiment is {sentiment}
        - tone is {tone}
        - urgency is {urgency}
        - type of the issue is {issueType}

        Generate a response from customer support team to the customer.
        """
     response= structured_model.invoke(prompt)
     return {'response': response}
37/143:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/144:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/145: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/146:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/147:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/148: load_dotenv()
37/149:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/150:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/151:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/152: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/153:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/154:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/155:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= structured_model.invoke(prompt)
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review.
        - sentiment is {sentiment}
        - tone is {tone}
        - urgency is {urgency}
        - type of the issue is {issueType}

        Generate a response from customer support team to the customer.
        """
     response= structured_model.invoke(prompt).content
     return {'response': response}
37/156:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/157:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/158: review = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/159:
initial_state= {'review': review}

workflow.invoke(initial_state)
37/160:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/161: load_dotenv()
37/162:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/163:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/164:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/165: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/166:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/167:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/168:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= model.invoke(prompt).content
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review.
        - sentiment is {sentiment}
        - tone is {tone}
        - urgency is {urgency}
        - type of the issue is {issueType}

        Generate a response from customer support team to the customer.
        """
     response= structured_model.invoke(prompt).content
     return {'response': response}
37/169:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/170:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/171: review1 = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/172: review2 = '“I’m genuinely impressed with this laptop. It boots up instantly, runs multiple heavy applications without slowing down, and the battery easily lasts me through a full workday. The display is bright and crisp, and the keyboard feels great for long typing sessions. I also appreciate how quiet the fans are, even during video editing. Overall, this laptop has exceeded my expectations and has become one of the best purchases I’ve made for work and travel.'
37/173:
initial_state= {'review': review2}

workflow.invoke(initial_state)
37/174:
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
37/175: load_dotenv()
37/176:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
37/177:
class CustomerSupportSchema(BaseModel):
    tone: str = Field(description='tone of the review')
    sentiment: str = Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
    urgency: str = Field(description='Urgency of the issue of the review')
    issueType: str = Field(description= 'Type of the issue in the review')
37/178:
class SentimentSchema(BaseModel):
    sentiment: Literal['positive', 'negative']= Field(description="sentiment of the review. Sentiment should be one word either 'positive' or 'negative'")
37/179: structured_model = model.with_structured_output(CustomerSupportSchema, strict= True)
37/180:
prompt= f'What is the sentiment of the review - The software is too bad'

structured_model.invoke(prompt).sentiment
37/181:
class CustomerSupportState(TypedDict):
    issueType: str
    tone: str
    urgency: str
    sentiment: str
    review: str
    response: str
37/182:
def find_sentiment(state: CustomerSupportState):
    
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the sentiment of the review. The sentiment should be only one word -  'positive' or 'negative'.
            - review is {review}
            """
    sentiment = structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def run_diagnosis(state: CustomerSupportState):
    review = state['review']
    prompt = f"""
            Analyse the review of the customer and provide the tone, type of the issue, urgency
            - review is {review}
            """
    tone = structured_model.invoke(prompt).tone
    issueType = structured_model.invoke(prompt).issueType
    urgency = structured_model.invoke(prompt).urgency
    return {'tone': tone, 'issueType': issueType, 'urgency': urgency}

def positive_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     prompt = f"""
        Based on the sentiment of the review. Provide a positive response.
        - review is {review}
        - sentiment is {sentiment}
        """
     response= model.invoke(prompt).content
     return {'response': response}


def negative_response(state: CustomerSupportState):
     review = state['review']
     sentiment = state['sentiment']
     tone= state['tone']
     urgency= state['urgency']
     issueType= state['issueType']
     prompt = f"""
        Based on the sentiment, tone, type of issue, urgency of the review.
        - sentiment is {sentiment}
        - tone is {tone}
        - urgency is {urgency}
        - type of the issue is {issueType}

        Generate a response from customer support team to the customer.
        """
     response= model.invoke(prompt).content
     return {'response': response}
37/183:
def checkSentiment(state: CustomerSupportState)-> Literal['positive_response', 'run_diagnosis']:
    if state['sentiment'] == 'positive':
        return 'positive_response'
    else:
        return 'run_diagnosis'
37/184:
graph = StateGraph(CustomerSupportState)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', checkSentiment)
graph.add_edge('run_diagnosis', 'negative_response')
graph.add_edge('negative_response', END)
graph.add_edge('positive_response', END)

workflow = graph.compile()
workflow
37/185: review1 = 'This is the worst laptop I’ve ever purchased. Within weeks of buying it, the system started showing hardware problems — random shutdowns, keys falling off, and constant software glitches. The laptop became almost unusable right out of the box. When I contacted customer service, the experience was even worse. They were unhelpful, dismissive, and kept pushing me toward repairs instead of replacing a clearly defective product. After sending the laptop in, it came back in even worse condition and eventually became completely inoperable. I’ve been a loyal customer for years, but after this experience, I’m never buying from this brand again.'
37/186: review2 = '“I’m genuinely impressed with this laptop. It boots up instantly, runs multiple heavy applications without slowing down, and the battery easily lasts me through a full workday. The display is bright and crisp, and the keyboard feels great for long typing sessions. I also appreciate how quiet the fans are, even during video editing. Overall, this laptop has exceeded my expectations and has become one of the best purchases I’ve made for work and travel.'
37/187:
initial_state= {'review': review1}

workflow.invoke(initial_state)
38/1:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
38/2:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
38/3: load_dotenv()
38/4:
model = ChatOpenAI(
    
)
38/5:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/6:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/7: structured_model = model.with_structured_output(PostSchema)
38/8:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal
38/9:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
38/10: def generation
38/11:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/12:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state["topic"]}'

    post = model.invoke(prompt).content
    return {'post', post}
38/13:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/14:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state["topic"]}'

    post = model.invoke(prompt).content
    return {'post', post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}
38/15:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state["topic"]}'

    post = model.invoke(prompt).content
    return {'post', post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluationResult': evaluationResult}
38/16:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state["topic"]}'

    post = model.invoke(prompt).content
    return {'post', post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluationResult': evaluationResult}

def checkPostQuality(state: PostState)-> Literal['optimize']:

    if state['evaluation_result'] =='bad':
        return 'optimize'
38/17:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', evaluate)

graph.add_conditional_edge('evaluate', checkPostQuality)

graph.add_edge(checkPostQuality, END)
graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', evaluate)

workflow= graph.compile()
workflow
38/18:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', evaluate)

graph.add_conditional_edges('evaluate', checkPostQuality)

graph.add_edge(checkPostQuality, END)
graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', evaluate)

workflow= graph.compile()
workflow
38/19:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', evaluate)

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', evaluate)

workflow= graph.compile()
workflow
38/20:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', evaluate)

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/21:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/22:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/23:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/24: load_dotenv()
38/25:
model = ChatOpenAI(
    
)
38/26:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/27: structured_model = model.with_structured_output(PostSchema)
38/28:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/29:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post', post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluationResult': evaluationResult}

def checkPostQuality(state: PostState)-> Literal['optimize']:

    if state['evaluation_result'] =='bad':
        return 'optimize'
38/30:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/31:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/32:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/33: load_dotenv()
38/34:
model = ChatOpenAI(
    
)
38/35:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/36: structured_model = model.with_structured_output(PostSchema)
38/37:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/38:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluationResult': evaluationResult}

def checkPostQuality(state: PostState)-> Literal['optimize']:

    if state['evaluation_result'] =='bad':
        return 'optimize'
38/39:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/40:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/41:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/42: load_dotenv()
38/43:
model = ChatOpenAI(
    
)
38/44:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/45: structured_model = model.with_structured_output(PostSchema)
38/46:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/47:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState)-> Literal['optimize']:

    if state['evaluation_result'] =='bad':
        return 'optimize'
38/48:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/49:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/50:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/51: load_dotenv()
38/52:
model = ChatOpenAI(
    
)
38/53:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/54: structured_model = model.with_structured_output(PostSchema)
38/55:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/56:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState) -> Literal['optimize', '__end__']:
    if state['evaluation_result'] == 'bad':
        return 'optimize'
    return END
38/57:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/58:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/59:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/60: load_dotenv()
38/61:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
38/62:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/63: structured_model = model.with_structured_output(PostSchema)
38/64:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/65:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState) -> Literal['optimize', '__end__']:
    if state['evaluation_result'] == 'bad':
        return 'optimize'
    return END
38/66:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/67:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/68:
model = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
model2 = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
38/69:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/70: load_dotenv()
38/71:
model = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
model2 = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
38/72:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/73: structured_model = model1.with_structured_output(PostSchema)
38/74:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
38/75: load_dotenv()
38/76:
model = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
model1 = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
model2 = ChatOpenAI(
    model= 'gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)
38/77:
class PostSchema(BaseModel):
    evaluationResult: Literal['good', 'bad']
38/78: structured_model = model1.with_structured_output(PostSchema)
38/79:
class PostState(TypedDict):
    post: str
    optimized_post: str
    evaluation_result: Literal['good', 'bad']
    topic: str
38/80:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model2.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState) -> Literal['optimize', '__end__']:
    if state['evaluation_result'] == 'bad':
        return 'optimize'
    return END
38/81:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality)

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/82:
initial_state={
    'topic': 'Life'
}

workflow.invoke(initial_state)
38/83:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model2.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState) -> Literal['optimize', 'end']:
    if state['evaluation_result'] == 'bad':
        return 'optimize'
    else:
        return 'end'
38/84:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality,{'optimize':'optimize','end':END})

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
38/85:
def generation(state: PostState):
    
    prompt= f'Generate a post of 100 words on topic{state['topic']}'

    post = model.invoke(prompt).content
    return {'post': post}

def optimize(state: PostState):
    
    prompt = f'Optimize the post {state["post"]}'
    
    post= model2.invoke(prompt).content

    return {'post':post}

def evaluate(state: PostState):

    prompt = f'Evlauate the post{state["post"]}'

    evaluationResult = structured_model.invoke(prompt).evaluationResult

    return {'evaluation_result': evaluationResult}

def checkPostQuality(state: PostState) -> Literal['optimize1', 'end']:
    if state['evaluation_result'] == 'bad':
        return 'optimize1'
    else:
        return 'end'
38/86:
graph = StateGraph(PostState)
graph.add_node('generation', generation)
graph.add_node('optimize', optimize)
graph.add_node('evaluate', evaluate)

graph.add_edge(START, 'generation')
graph.add_edge('generation', 'evaluate')

graph.add_conditional_edges('evaluate', checkPostQuality,{'optimize1':'optimize','end':END})

#graph.add_edge(checkPostQuality, END)
#graph.add_edge(checkPostQuality, 'optimize')
graph.add_edge('optimize', 'evaluate')

workflow= graph.compile()
workflow
39/1:
from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
39/2: load_dotenv()
39/3:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
39/4:
model = ChatOpenAI(
    
)
39/5:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import os
39/6:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
import os
39/7:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/8:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
import os
39/9:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/10:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'message': response}
39/11:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'message': [response]}
39/12:
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile()

chatbot
39/13:
initial_state={
    'messages': [HumanMessage(content='What is the capital of India')]
}

chatbot.invoke(initial_state)
39/14:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
import os
39/15: load_dotenv()
39/16:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")

)
39/17:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/18:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'messages': [response]}
39/19:
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile()

chatbot
39/20:
initial_state={
    'messages': [HumanMessage(content='What is the capital of India')]
}

chatbot.invoke(initial_state)
39/21:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
import os
39/22: load_dotenv()
39/23:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")

)
39/24:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/25:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'messages': [response]}
39/26:
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile()

chatbot
39/27:
initial_state={
    'messages': [HumanMessage(content='What is the capital of India')]
}

chatbot.invoke(initial_state)['messages'][-1].content
39/28:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke('message': [HumanMessage(content= user_message)])

    print('AI: ' response['message'][-1].content)
39/29:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'message': [HumanMessage(content= user_message)]})

    print('AI: ' response['message'][-1].content)
39/30:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'message': [HumanMessage(content= user_message)]})

    print('AI: ', response['message'][-1].content)
39/31:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]})

    print('AI: ', response['messages'][-1].content)
39/32:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]})

    print('AI: ', response['messages'].content)
39/33:
while True:
    user_message = input('Type Here: ')

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]})

    print('AI: ', response['messages'])
39/34:
while True:
    user_message = input('Type Here: ')

    print('User: ', user_message)

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]})

    print('AI: ', response['messages'][-1]  .content)
39/35:
/*
initial_state={
    'messages': [HumanMessage(content='What is the capital of India')]
}

chatbot.invoke(initial_state)['messages'][-1].content
*/
39/36:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
import os
39/37: load_dotenv()
39/38:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")

)
39/39:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/40:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'messages': [response]}
39/41:
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile()

chatbot
39/42:

# initial_state={
#     'messages': [HumanMessage(content='What is the capital of India')]
# }

# chatbot.invoke(initial_state)['messages'][-1].content
39/43:
while True:
    user_message = input('Type Here: ')

    print('User: ', user_message)

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break

    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]})

    print('AI: ', response['messages'][-1]  .content)
39/44:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import os
39/45:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import os
39/46: load_dotenv()
39/47:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")

)
39/48:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/49:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'messages': [response]}
39/50:
checkpointer = MemorySaver()
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer = checkpointer)

chatbot
39/51:

# initial_state={
#     'messages': [HumanMessage(content='What is the capital of India')]
# }

# chatbot.invoke(initial_state)['messages'][-1].content
39/52:
thread_id = '1'
while True:
    user_message = input('Type Here: ')

    print('User: ', user_message)

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break
    
    config = {'configurable': {'thread_id': thread_id}}
    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]}, config = config)

    print('AI: ', response['messages'][-1]  .content)
39/53:
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import os
39/54: load_dotenv()
39/55:
model = ChatOpenAI(
    model= 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")

)
39/56:
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
39/57:
def chat_node(state: ChatState):

    message = state['messages']

    response = model.invoke(message)

    return {'messages': [response]}
39/58:
checkpointer = MemorySaver()
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer = checkpointer)

chatbot
39/59:

# initial_state={
#     'messages': [HumanMessage(content='What is the capital of India')]
# }

# chatbot.invoke(initial_state)['messages'][-1].content
39/60:
thread_id = '1'
while True:
    user_message = input('Type Here: ')

    print('User: ', user_message)

    if(user_message.strip().lower() in ['exit', 'quit', 'bye']):
        break
    
    config = {'configurable': {'thread_id': thread_id}}
    response = chatbot.invoke({'messages': [HumanMessage(content= user_message)]}, config = config)

    print('AI: ', response['messages'][-1]  .content)
45/1: %history -g
45/2: !python --version
   1: .ipynb_checkpoints/
   2: %history -g
