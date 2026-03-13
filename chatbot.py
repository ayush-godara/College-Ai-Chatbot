from groq import Groq
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def search_links(query):
    links = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            links.append(r["href"])

    return links


def extract_page_text(url):

    try:
        response = requests.get(url, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return text[:4000]

    except:
        return ""


def ask_question(query):

    search_query = "BMS College of Engineering Bangalore " + query

    links = search_links(search_query)

    context = ""

    for link in links:
        context += extract_page_text(link)

    prompt = f"""
You are an AI assistant for BMS College of Engineering (BMSCE).

Use the website content below to answer the question accurately.

Website Content:
{context}

Question:
{query}

Give a factual answer and mention if the information comes from the BMSCE website.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content