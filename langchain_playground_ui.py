import gradio as gr
from .langchain_playground_params import lp_ui_elements
from .langchain_playground_operation import LangChainOperation

def generate_gradio_ui():
    with gr.Row():
        with gr.Column():
            with gr.Row():
                with gr.Tab('Text'):
                    with gr.Row():
                        lp_ui_elements["writer_pad_textbox"] = gr.Textbox(value='', elem_classes="textbox", lines=20, label = 'Writer Pad')
            with gr.Row():
                lp_ui_elements["generate_btn"] = gr.Button('Generate', variant='primary', elem_classes="small-button")

def generate_button_callbacks():
    langchain_operation = LangChainOperation("conversation_summary_memory")
    lp_ui_elements["generate_btn"].click(langchain_operation.execute_langchain, lp_ui_elements["writer_pad_textbox"])