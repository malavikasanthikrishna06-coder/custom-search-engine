from search import search_web
from llm import generate_answer


def main():
    print("\n" + "=" * 55)
    print("           🕵️ CUSTOM AI SEARCH ENGINE")
    print("=" * 55)
    print("Type 'exit' to quit.")

    while True:
        query = input("\n🔎 Search: ").strip()

        if query.lower() == "exit":
            print("\n👋 Thanks for using Custom AI Search Engine!")
            break

        if not query:
            print("❌ Please enter a search query.")
            continue

        print("\n🌐 Searching the web...")

        try:
            results = search_web(query)

            if not results:
                print("❌ No results found.")
                continue

            print(f"✅ Found {len(results)} results.")
            print("🤖 Generating AI answer...")

            answer = generate_answer(query, results)

            print("\n" + "=" * 55)
            print("                    🤖 AI ANSWER")
            print("=" * 55)
            print(answer)

            print("\n" + "=" * 55)
            print("                  📚 WEB SOURCES")
            print("=" * 55)

            for i, result in enumerate(results, start=1):
                print(f"\n{i}. {result['title']}")
                print(f"   🔗 {result['url']}")

        except Exception as e:
            print(f"\n❌ Something went wrong: {e}")


if __name__ == "__main__":
    main()