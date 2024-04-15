import gradio as gr
from db import execute_query

def welcome(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    with gr.Row():
        inp = gr.Textbox(placeholder="What query do you want to execute")
        out = gr.HTML(label="Highlighted SQL")
    out2 = gr.Dataframe(label="Query Result")
    inp.submit(execute_query, inp, [out,out2])

if __name__ == "__main__":
    demo.launch()
	
