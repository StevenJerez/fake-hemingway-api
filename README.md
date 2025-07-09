Lo siento, pero el lienzo no está disponible en este momento. Aquí tienes de nuevo el `README.md` en formato Markdown; puedes copiarlo directamente a tu repositorio:

```markdown
# Hemingway-like API

A RESTful service that analyzes text readability, provides style suggestions (adverbs, passive voice, complex phrases, qualifiers), and offers a simple rewrite feature.

## 🚀 Features

- **/analyze**  
  Returns counts of paragraphs, sentences, words, letters, adverbs, passive constructions, complex phrases, qualifiers, and a readability score.
- **/suggest**  
  Returns a list of style suggestions: spans flagged as adverb, passive voice, complex phrase, or qualifier.
- **/rewrite**  
  Applies first-pass simplifications: removes adverbs and qualifiers, converts passive → active prompts, replaces one complex phrase.

## 📁 Project Structure

```

hemingway-api/
├── analyzer.py         # Core analysis & rewrite logic
├── main.py             # FastAPI application & endpoints
├── schemas.py          # Pydantic request/response models
├── test\_api.py         # pytest test suite
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container definition
└── README.md           # This documentation

````

## 🔧 Requirements

- Python 3.11+
- pip
- (Optionally) Docker & Docker Compose
- pytest (for running tests)

## 💻 Local Setup

1. **Clone repository & enter directory**  
   ```bash
   git clone https://github.com/yourusername/hemingway-api.git
   cd hemingway-api
````

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the API server**

   ```bash
   uvicorn main:
   ```