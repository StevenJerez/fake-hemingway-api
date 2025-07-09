# Fake Hemingway API

A RESTful API service that analyzes and suggests improvements for English text, inspired by Hemingway Editor. Built with FastAPI and containerized with Docker.

## Features

* **Analyze** reading difficulty metrics: readability score, hard/very-hard sentences, adverb count, passive voice count, complex phrase count.
* **Suggest** specific improvements (planned).
* **Rewrite** text based on a target style (planned).
* **Lightweight** with no external dependencies beyond requirements.

## Project Structure

```
fake-hemingway-api/
├── app/
│   ├── main.py           # FastAPI application with endpoints
│   ├── analyzer.py       # Core analysis logic ported from JS
│   └── schemas.py        # Pydantic models for request/response
├── tests/
│   └── test_api.py       # Unit tests using pytest
├── Dockerfile            # Docker image definition
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Requirements

* Python 3.8+
* Docker (for containerized deployment)

## Installation & Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-org/fake-hemingway-api.git
   cd fake-hemingway-api
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run tests**:

   ```bash
   pytest
   ```

5. **Start the server**:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## Docker Deployment

Build and run with Docker:

```bash
docker build -t fake-hemingway-api .
docker run --rm -p 8000:8000 fake-hemingway-api
```

Your API is available at `http://localhost:8000`.

## API Endpoints

### Analyze Text

* **URL**: `/analyze`
* **Method**: `POST`
* **Request Body**:

  ```json
  {
    "text": "Your text to analyze"
  }
  ```
* **Response**:

  ```json
  {
    "readability_score": 8.23,
    "adverb_count": 2,
    "passive_voice_count": 1,
    "complex_count": 3,
    "hard_sentences": 0,
    "very_hard_sentences": 0
  }
  ```

*Future endpoints for `/suggest` and `/rewrite` will follow similar patterns.*

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add YourFeature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
