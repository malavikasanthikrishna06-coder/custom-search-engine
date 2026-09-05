import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)


def generate_answer(query, search_results):

    context = "\n\n".join(
        [
            f"Title: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content: {result['content']}"
            for result in search_results
        ]
    )

    prompt = f"""
You are a reliable AI search assistant.

The user asked:

{query}

Below are web search results:

{context}

Your task:

1. Answer the user's question directly.
2. Use the provided search results as your factual context.
3. Do not invent information that is not supported by the results.
4. Explain technical concepts in simple language when appropriate.
5. If the search results disagree, mention the disagreement.
6. Keep the answer well structured and concise.
7. Use headings or bullet points when they improve readability.
8. At the end, provide the most relevant sources.

Format:

ANSWER:
<your answer>

SOURCES:
1. <source title> — <URL>
2. <source title> — <URL>
3. <source title> — <URL>
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text