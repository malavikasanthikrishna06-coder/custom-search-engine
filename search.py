import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY is missing from .env")

client = TavilyClient(api_key=api_key)


def search_web(query, max_results=5):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results
    )

    results = []

    for result in response.get("results", []):
        results.append({
            "title": result.get("title", "No title"),
            "url": result.get("url", ""),
            "content": result.get("content", "")
        })

    return results