import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import Markdown

load_dotenv()
GEMINI_KEY = os.getenv('gemini_key')

genai.configure(api_key = GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def genai_upload(file_path):
    file = genai.upload_file(file_path)
    return file

def generate_response(query, file):
    response = model.generate_content([file, f'\n\nAnswer the following query based on the provided document, remember to STRICTLY NOT ANSWER any query that is unrelated to the provided document. The query is - {query}'])
    return response.text

response = model.generate_content(["smartwatch.jpg", "This image is from an instagram post and contains a product. Generate a SEO-friendly and user-centric Amazon product listing for it. The following is the post's caption - 'Apple Watch Series 7 \nRs. 49,900 \nFeatures: Wifi 5 support, sleep tracking, blood oxygen monitor, heart rate monitor.'"])
# print(response.text)
for chunk in response:
    print(chunk.text, end="")