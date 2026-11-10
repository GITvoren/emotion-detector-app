# Emotion Detection Web Application

A full-stack web application built with Python and Flask that analyzes user-submitted text to detect underlying emotional tones (anger, disgust, fear, joy, and sadness) and identifies the dominant emotion using the IBM Watson Natural Language Processing (NLP) API.

![Pylint Score](https://img.shields.io/badge/Pylint-10.00%2F10-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)

---

## Key Features

- **Watson NLP Integration:** Leverages pre-trained emotion-classification models to analyze natural language text inputs.
- **Dynamic Flask Backend:** Serves clean RESTful web endpoints and renders an interactive web interface.
- **Comprehensive Error Handling:** Gracefully handles invalid inputs and HTTP 400 bad requests by detecting empty payload responses and warning the user.
- **Modular Package Architecture:** Encapsulates API request logic within a standalone, reusable `EmotionDetection` Python package.
- **Automated Unit Testing:** Includes a dedicated test suite built with `unittest` to ensure robust emotion classification.
- **Production-Grade Code Standards:** Fully compliant with PEP 8 standards, achieving a **10.00/10 Pylint score**.

---

## Tech Stack

- **Language:** Python 3
- **Web Framework:** Flask
- **External API:** IBM Watson NLP Emotion Predict Service
- **Testing & Tooling:** `unittest`, `pylint`, `requests`

---

## Project Structure

```text
.
├── EmotionDetection/
│   ├── __init__.py           # Package initializer
│   └── emotion_detection.py  # Watson API client and response parser logic
├── static/                   # CSS and JavaScript assets
├── templates/
│   └── index.html            # Main web page interface
├── server.py                 # Flask server and web route definitions
├── test_emotion_detection.py # Automated unit test suite
└── README.md                 # Project documentation
```

---

## Execution & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/emotion-detector-app.git
   cd emotion-detector-app
   ```

2. **Install required packages:**
   ```bash
   pip install flask requests pylint
   ```

3. **Launch the Flask application:**
   ```bash
   python3 server.py
   ```

4. **Access the Web Interface:**
   Open your browser and navigate to `http://127.0.0.1:5000` or `http://localhost:5000`.

---

## Testing & Quality Assurance

### Running Unit Tests
To verify the application logic against test cases (confirming joy, anger, disgust, sadness, and fear detection):
```bash
python3 test_emotion_detection.py
```

### Static Code Analysis (Pylint)
To verify code formatting, docstring coverage, and adherence to PEP 8 standards:
```bash
pylint EmotionDetection/emotion_detection.py server.py
```
**Output:**
```text
-------------------------------------------------------------------
Your code has been rated at 10.00/10
```

---

## API Environment Note

*This application relies on an IBM Watson NLP API endpoint configured for the IBM Skills Network lab environment. Live deployment outside of the lab environment requires adjusting the API endpoint URL or replacing it with an equivalent open-source NLP classifier model (such as Hugging Face Transformers).*

---

## Author
Developed as part of the **IBM Applied Artificial Intelligence** Capstone Curriculum.