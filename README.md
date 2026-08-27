# LinkedIn Post Generator

An AI-powered automation tool designed to generate highly engaging, tailored LinkedIn posts. By leveraging Large Language Models (LLMs) alongside advanced few-shot prompting techniques, this project analyzes historical post structures and automatically curates high-impact professional content matched to specific topics, tones, and lengths.

\---

# Tech Stack \& Core Libraries

* **\[LangChain]**: Orchestrates the few-shot prompt management, chat model interfaces, and chain execution.
* **\[OpenAI API]**: Powers the primary semantic understanding and context-aware post generation via advanced GPT models.
* **\[Pandas]**: Manages data manipulation, structured reading, and indexing of historical post datasets.



\---

# Project Structure

```text
linkedin\\\_post\\\_gen/
│
├── Data/
│   ├── raw\\\_posts.json           # Ingested unformatted historical posts
│   └── processed\\\_posts.json     # Cleaned, tokenized, and tagged post vectors
│
├── \\\_\\\_pycache\\\_\\\_/                # Compiled bytecode files
├── .env                        # Environment configuration (API Keys \\\& parameters)
├── few\\\_shot.py                 # Dynamically fetches the best contextual examples
├── llm\\\_helper.py               # Handles model initializations and wrapper instances
├── main.py                     # Primary Application Command Line Interface (CLI)
├── post\\\_generator.py           # Constructs dynamic few-shot templates and chains
└── preprocess.py               # Sanitizes, filters, and prepares raw text files
```

\---

# Component Workflow

1. **`preprocess.py`**: Ingests `raw\\\_posts.json`, extracts metadata tags, cleans formatting anomalies, and structures output into `processed\\\_posts.json`.
2. **`few\\\_shot.py`**: Implements similarity searches or rule-based filtering to select the most relevant historical posts to inject as contextual examples.
3. **`llm\\\_helper.py`**: Configures downstream endpoints, handles retry logic, and sets up authentication structures for the OpenAI client.
4. **`post\\\_generator.py`**: Merges selected few-shot examples with the current prompt topic to generate cohesive, human-like output drafts.
5. **`main.py`**: Serves as the central user entry point to configure runs directly via terminal arguments.

\---

# Installation \& Setup

1. Clone the Repository

```bash
git clone https://github.com/your-username/linkedin\\\_post\\\_gen.git
cd linkedin\\\_post\\\_gen
```

2. Configure Environment Variables
Create a `.env` file in the root directory:

```env
OPENAI\\\_API\\\_KEY=your\\\_openai\\\_api\\\_key\\\_here
LLM\\\_MODEL=gpt-4o
DEFAULT\\\_TEMPERATURE=0.7
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

\---

# Usage \& CLI Reference

Run the application through `main.py` using terminal arguments to customize output properties:

```bash
python main.py --topic "Artificial Intelligence" --tone "Thought Leadership" --length "Medium"
```



\---

# Example Generation

# Input Command:

```bash
python main.py --topic "Remote Work Productivity" --length "Short"--language "English" 
```

# Sample Output:

```text
The office isn't a place anymore—it's a mindset. 🌐

After transitioning my team to 100% remote work, I realized productivity isn't about counting hours spent in a desk chair. It's about counting outcomes achieved in deep focus. 

Three things that changed our velocity:
1. Asynchronous status updates (fewer soul-crushing meetings).
2. Defined "Deep Work" blocks on public calendars.
3. Radical ownership over deliverables, not clock-in times.

Trust your team, measure the output, and watch what happens. 

```

\---



