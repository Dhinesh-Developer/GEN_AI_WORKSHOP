import sqlite3 as sql
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = "AIzaSyDAoDpCjhMRbLaMi4kkB5zvYXVQYcAnq6s"
# Configure the GenAI API
key = os.getenv("GOOGLE_API_KEY")
if not key:
    raise ValueError("API key not found. Please set 'GOOGLE_API_KEY' in your .env file.")
genai.configure(api_key=key)

# Function to initialize the database and insert data
def initialize_database():
    connection = sql.connect("employee.db")
    cursor = connection.cursor()
    
    # Uncomment the next line if the table doesn't already exist
    # cursor.execute("CREATE TABLE employees (empid INT, empname VARCHAR(20), empsalary INT, empdesignation VARCHAR(20))")
    
    cursor.execute("INSERT INTO employees VALUES (1, 'kumar', 100000, 'Developer')")
    cursor.execute("INSERT INTO employees VALUES (2, 'badri', 200000, 'HR')")
    cursor.execute("INSERT INTO employees VALUES (3, 'damo', 30000, 'Manager')")
    cursor.execute("INSERT INTO employees VALUES (4, 'ameer', 40000, 'Realist')")
    connection.commit()
    connection.close()

# Function to get SQL query from Gemini model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    res = model.generate_content(f"{prompt}\nQuestion: {question}")
    return res.text.strip()

# Function to execute the SQL query
def hit_sql_database(query, db):
    connection = sql.connect(db)
    cursor = connection.cursor()
    try:
        data = cursor.execute(query)
        for row in data:
            print(row)
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()

# Initialize the database (comment out if already initialized)
# initialize_database()

# Define the prompt and question
prompt = """
You are an expert in converting natural language questions into SQL queries.
The SQL database 'employee.db' contains a table named 'employees' with the following columns:
- empid
- empname
- empsalary
- empdesignation

For example:
1. To select all columns: SELECT * FROM employees;
2. To select employee names with a salary greater than 10000: SELECT empname FROM employees WHERE empsalary > 10000;

Your task is to generate an SQL query based on the question below without including 'SQL' in the output or enclosing the query in quotes.
"""
question = "select names of the employees whose name starts with 'd'"

# Get the SQL query from Gemini
response_query = get_gemini_response(question, prompt)
print(f"Generated Query: {response_query}")

# Execute the query on the database
hit_sql_database(response_query, "employee.db")
