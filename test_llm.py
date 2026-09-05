from llm import generate_answer

results = [
    {
        "title": "Example",
        "url": "https://example.com",
        "content": "Artificial intelligence allows computers to perform tasks that normally require human intelligence."
    }
]

answer = generate_answer(
    "What is artificial intelligence?",
    results
)

print("\n🤖 Gemini Answer:\n")
print(answer)