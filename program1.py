import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

load_dotenv()

import os
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-pro")
# print(model)


question = input("Ask a question")

def get_answer(question):
    res = model.generate_content(question)
    print(res)

get_answer(question)







'''' genai.configure(api_key="")
model = genai.GenerativeModel("gemini-pro")
res = model.generate_content("who is the founder of apple")
print(res.text)'''
