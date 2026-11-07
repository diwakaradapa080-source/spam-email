# Spam Email Classifier Using Machine Learning

A beginner-friendly Flask web application that classifies email text as **SPAM** or **NOT SPAM (HAM)** using TF-IDF features and a Multinomial Naive Bayes classifier.

## Project files

- `app.py` — Flask web application and prediction logic
- `train_model.py` — trains and saves the model
- `data/spam.csv` — small included demonstration dataset
- `templates/index.html` — web interface
- `static/css/style.css` — page styling
- `requirements.txt` — Python dependencies
- `model/` — trained model is generated automatically

## Run in Antigravity (or a local terminal)

1. Upload/extract the complete `spam_email_classifier` folder.
2. Open that folder as the project/workspace.
3. Open the terminal in that folder.
4. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
6. Start the application:
   ```bash
   python app.py
   ```
7. Open `http://127.0.0.1:5000` in your browser.

The model is trained automatically the first time the app starts. To retrain it after changing the CSV:
```bash
python train_model.py
```

## Dataset format

`data/spam.csv` must have exactly these required column names:
- `label`: `spam` or `ham`
- `message`: email/message text

Add more labelled examples to improve model quality. The included dataset is a **small demonstration dataset**, not a production-grade or academically sufficient benchmark. For a final-year submission, use a larger, properly sourced and documented dataset, then evaluate on a held-out test set.

## API / health check

- `GET /health` returns a small JSON status response.
- The main prediction interface is available at `/`.

## Notes

- No NLTK download is required.
- No external API key or internet connection is required after dependencies are installed.
- Model confidence is the classifier's maximum predicted class probability; it is not a guarantee that the prediction is correct.
