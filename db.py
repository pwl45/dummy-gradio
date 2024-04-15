import psycopg2
from psycopg2 import Error
import time

from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import HtmlFormatter

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
    formatted_sql = highlight(query, SqlLexer(), HtmlFormatter(full=True, style='colorful'))
    loading_message=str(formatted_sql)
    yield formatted_sql,None
    conn = connect_to_db()
    if conn is None:
        return "Error connecting to the database"
    time.sleep(1)
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
        
        print(f'returning {result}')
        yield formatted_sql,result
    except Error as e:
        yield formatted_sql,None
