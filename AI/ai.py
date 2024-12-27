import os
import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv


load_dotenv()
# key = "AIzaSyDpCVvGau4ZSp7Ht8rDS7otm3RZeTGD8dw"
key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")
res = model.generate_content("In which year ai is peak? why upto which year it is peak?")
print(res.text)

