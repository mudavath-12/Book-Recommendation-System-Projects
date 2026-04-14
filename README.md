# 📚 Bibliophile — Book Recommendation System

A machine learning-powered book recommender built using **Flask + TF-IDF + Cosine Similarity**.

---

## 🚀 Features

- 🔍 Search books by **title or author**
- 🤖 Smart recommendations using **Machine Learning**
- 📖 View book details (description, rating, price)
- 🏷️ Filter books by **genre**
- 💻 Clean and responsive web interface

---

## 🧠 How It Works

1. **TF-IDF Vectorization**
   - Converts book descriptions, tags, genre, and author into numerical vectors

2. **Cosine Similarity**
   - Calculates similarity between books

3. **Recommendation System**
   - Suggests top similar books based on user selection

---

## ⚙️ Technologies Used

- Python
- Flask
- Scikit-learn
- NumPy
- HTML, CSS, JavaScript

---

## 📁 Project Structure
book_recommender/
│── app.py
│── books_data.py
│── requirements.txt
│── README.md
│── templates/
└── index.html

---

## ▶️ How to Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
