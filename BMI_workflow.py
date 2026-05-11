# 2_bmi_graph.py

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image

# Define state
class BMIState(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float
    label: str

def calculate_bmi(state: BMIState) -> BMIState:
    weight = state["weight_kg"]
    height = state["height_m"]
    bmi = weight / (height ** 2)
    state["bmi"] = round(bmi, 2)
    return state

def label_bmi(state: BMIState) -> BMIState:
    bmi = state["bmi"]
    if bmi > 30:
        state["label"] = "obese"
    elif 25 <= bmi <= 30:
        state["label"] = "overweight"
    elif 18.5 <= bmi < 25:
        state["label"] = "normal"
    else:
        state["label"] = "underweight"
    return state

# Build graph
graph = StateGraph(BMIState)
graph.add_node("calculate_bmi", calculate_bmi)
graph.add_node("label_bmi", label_bmi)

graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", "label_bmi")
graph.add_edge("label_bmi", END)

workflow = graph.compile()

# Execute
initial_state = {"weight_kg": 80, "height_m": 1.73}
final_state = workflow.invoke(initial_state)
print(final_state)

# Visualize (if graphviz etc. installed)
try:
    img = workflow.get_graph().draw_mermaid_png()
    display(Image(img))
except Exception as e:
    print("Graph visualization not available:", e)
