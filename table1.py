import gradio as gr
import psycopg2
import pandas as pd
from psycopg2 import Error
import time

# Connect to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="myuser",
            password="mypass"
        )
        return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def execute_query(query):
    loading_message = f"Running query {query}"
    yield loading_message,None
    conn = connect_to_db()
    if conn is None:
        return "Error connecting to the database"
    time.sleep(3)
    try:
        cur = conn.cursor()
        cur.execute(query)
        
        # Fetch all rows from the result
        rows = cur.fetchall()
        
        # Get the column names
        col_names = [desc[0] for desc in cur.description]
        result = {
            'headers':col_names,
            'data':rows,
        }
        
        
        cur.close()
        conn.close()
        
        yield loading_message,result
    except Error as e:
        yield loading_message,None

# Gradio interface
input_text = gr.Textbox(label="Enter SQL Query")
output_table = gr.Dataframe(label="Query Result")
output_text = gr.Textbox(label="Execution Result")

gr.Interface(
    fn=execute_query,
    inputs=input_text,
    outputs=[output_text,output_table],
    title="PostgreSQL Query Executor",
    description="Enter a SQL query and execute it against the PostgreSQL database."
).launch()
