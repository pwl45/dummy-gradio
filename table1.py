import gradio as gr
from db import execute_query

# Gradio interface
input_text = gr.Textbox(label="Enter SQL Query")
output_table = gr.Dataframe(label="Query Result")
# output_text = gr.Textbox(label="Status")
output_html = gr.HTML(label="Highlighted SQL")

gr.Interface(
    fn=execute_query,
    inputs=input_text,
    outputs=[output_html,output_table],
    title="PostgreSQL Query Executor",
    description="Enter a SQL query and execute it against the PostgreSQL database."
).launch()
