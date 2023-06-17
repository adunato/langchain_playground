import pickle
from .langchain_playground_ui import generate_button_callbacks, generate_gradio_ui

try:
    with open('notebook.sav', 'rb') as f:
        params = pickle.load(f)
except FileNotFoundError:
    params = {
        "display_name": "Langchain Playground",
        "is_tab": True,
        "usePR": False,
        "pUSER": 'USER:',
        "pBOT": 'ASSISTANT:',
        # "selectA": [0,0]
    }

def ui():
    generate_gradio_ui()
    generate_button_callbacks()
    
