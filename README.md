# Hemingway-like API

A RESTful service that analyzes text readability, provides style suggestions (adverbs, passive voice, complex phrases, qualifiers), and offers a simple rewrite feature.

## 🚀 Features

- **POST `/analyze`**  
  Returns:
  - `paragraphs`: number of paragraphs  
  - `sentences`: number of sentences  
  - `words`: number of words  
  - `adverbs`: count of adverbs  
  - `passive`: count of passive‐voice constructions  
  - `complex`: count of complex phrases  
  - `qualifiers`: count of weakening/qualifier phrases  
  - `readability_score`: Flesch Reading Ease (0–100+)

- **POST `/suggest`**  
  Returns a list of style suggestions:
  - `type`: one of `adverb` | `passive` | `complex` | `qualifier`  
  - `suggestion`: human‐readable advice  

- **POST `/rewrite`**  
  Returns one simple rewrite:
  - removes the first adverb/qualifier  
  - prompts active voice for the first passive instance  
  - replaces one complex phrase  

## 📁 Project Structure

```

hemingway-api/
├── app/
│   ├── **init**.py
│   ├── analyzer.py      # Core logic, now using textstat for readability
│   ├── main.py          # FastAPI app & endpoints
│   └── schemas.py       # Pydantic models
├── test\_api.py          # pytest suite
├── requirements.txt     # Python deps, incl. textstat
├── Dockerfile           # Container build instructions
└── README.md            # This file

````

## 🔧 Requirements

- Python 3.11+  
- pip  
- Docker (optional, for containerized deployment)  
- pytest (for running tests)

## 💻 Local Setup

1. **Clone & enter**  
   ```bash
   git clone https://github.com/yourusername/hemingway-api.git
   cd hemingway-api

2. **Create & activate venv**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run server**

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Try analyze**

   ```bash
   curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"text":"The sun is bright. It warms our planet each day."}'
   ```

## 🐳 Docker Usage

1. **Build image**

   ```bash
   docker build -t hemingway-api .
   ```

2. **Run container**

   ```bash
   docker run -p 8000:8000 hemingway-api
   ```

3. **Access API** at `http://localhost:8000`

## 📖 API Reference

### POST `/analyze`

**Request**

```json
{ "text": "Your text here." }
```

**Response**

```json
{
  "paragraphs": 1,
  "sentences": 2,
  "words":  nine,
  "adverbs": 0,
  "passive": 0,
  "complex": 0,
  "qualifiers": 0,
  "readability_score": 92.5
}
```

### POST `/suggest`

**Request**

```json
{ "text": "I believe the project was completed quickly." }
```

**Response**

```json
{
  "suggestions": [
    {
      "offset": null,
      "length": 8,
      "type": "qualifier",
      "suggestion": "Consider removing qualifier 'i believe'"
    },
    {
      "offset": null,
      "length": 7,
      "type": "adverb",
      "suggestion": "Avoid the adverb 'quickly'"
    }
  ]
}
```

### POST `/rewrite`

**Request**

```json
{ "text": "I believe the project was completed quickly by the team." }
```

**Response**

```json
{
  "rewritten_text": "The project was completed by the team."
}
```

## ✅ Testing

Run all tests:

```bash
pytest
```

## 🤝 Contributing

1. Fork this repo
2. Create a branch: `git checkout -b feature/xyz`
3. Commit & push: `git push origin feature/xyz`
4. Open a Pull Request

Please add tests for any new functionality.
