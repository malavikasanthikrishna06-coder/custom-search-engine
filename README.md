# 🕵️ Custom AI Search Engine

An AI-powered search engine built with **Python, Tavily Search API, and Google Gemini**.

Instead of simply returning a list of web pages, this project searches the web and uses an LLM to generate a clear, contextual answer based on the retrieved results.

---

## ✨ Features

* 🔎 Real-time web search using Tavily
* 🤖 AI-generated answers using Google Gemini
* 📚 Displays the sources used for each search
* 💻 Interactive command-line interface
* 🔁 Supports multiple searches in a single session
* 🛡️ API keys stored securely using environment variables
* ⚠️ Basic error and empty-query handling

---

## 🧠 How It Works

```text
                User Query
                    │
                    ▼
             ┌──────────────┐
             │  Python CLI  │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ Tavily Search│
             │     API      │
             └──────┬───────┘
                    │
              Web Results
                    │
                    ▼
             ┌──────────────┐
             │ Google Gemini│
             │     LLM      │
             └──────┬───────┘
                    │
                    ▼
          AI Answer + Sources
```

---

## 🛠️ Tech Stack

| Technology      | Purpose                              |
| --------------- | ------------------------------------ |
| Python          | Core programming language            |
| Tavily API      | Web search and information retrieval |
| Google Gemini   | AI answer generation                 |
| `requests`      | HTTP requests                        |
| `python-dotenv` | Environment variable management      |
| Git & GitHub    | Version control                      |

---

## 📂 Project Structure

```text
custom-search-engine/
│
├── app.py              # Main CLI application
├── search.py           # Tavily web search functionality
├── llm.py              # Gemini LLM integration
├── test_llm.py         # LLM testing
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/custom-search-engine.git
cd custom-search-engine
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

**Never commit your `.env` file or expose your API keys publicly.**

---

## 🚀 Usage

Run the application:

```bash
python app.py
```

Enter a question when prompted:

```text
=======================================================
           🕵️ CUSTOM AI SEARCH ENGINE
=======================================================
Type 'exit' to quit.

🔎 Search: How is edge AI different from cloud AI?
```

The application will:

1. Send the query to Tavily.
2. Retrieve relevant web results.
3. Send the results to Gemini.
4. Generate an AI-powered answer.
5. Display the relevant source URLs.

To quit:

```text
exit
```

---

## 🧪 Example Queries

Try questions such as:

```text
What is Edge AI?

How does RAG work?

How are CNNs used in computer vision?

What are the advantages of IoT?

How does YOLO object detection work?
```

---

## 🔐 Environment Variables

The following environment variables are required:

| Variable         | Description                   |
| ---------------- | ----------------------------- |
| `TAVILY_API_KEY` | API key for Tavily web search |
| `GEMINI_API_KEY` | API key for Google Gemini     |

These are loaded using `python-dotenv`.

---

## 📌 Current Limitations

This is an initial version of the project.

Future improvements could include:

* 🎯 Better source ranking
* 🔗 Inline citations
* 🧠 Conversation memory
* 📝 Search history
* ⚡ Query optimization
* 🌐 Web-based interface
* 📊 Search analytics
* 🔄 Retrieval-Augmented Generation (RAG)
* 🗂️ Source credibility scoring
* 🎨 Streamlit frontend

---

## 🔮 Future Roadmap

```text
[x] Python CLI
[x] Tavily web search
[x] Gemini integration
[x] AI-generated answers
[x] Source display
[ ] Source-aware citations
[ ] Search history
[ ] Conversation memory
[ ] RAG pipeline
[ ] Streamlit UI
[ ] Deployment
```

---

## 🎓 Learning Outcomes

Through this project, I explored:

* API integration
* Web information retrieval
* Large Language Models
* Prompt engineering
* Environment variable management
* Python project structure
* CLI application development
* Git and GitHub workflow

---

## 👩‍💻 Author

**Malavika S**

AI & ML Engineering Student

Interested in **Artificial Intelligence, Machine Learning, Computer Vision, IoT, Robotics, and Web Development**.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.
