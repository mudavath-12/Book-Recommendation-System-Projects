from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

API_KEY = "AIzaSyDD6hs0NVBcTYRuCAgJ5w4mS68AoMgAl0Q"


# -------------------------------
# Clean HTML from description
# -------------------------------
def clean_text(text):
    if not text:
        return "No description available."
    clean = re.sub('<.*?>', '', text)
    return clean


# -------------------------------
# Extract book data
# -------------------------------
def extract_books(data):
    books = []
    items = data.get("items", [])

    for item in items:
        volume = item.get("volumeInfo", {})
        sale = item.get("saleInfo", {})

        raw_description = volume.get("description", "No description available.")
        clean_description = clean_text(raw_description)

        books.append({
            "id": item.get("id"),
            "title": volume.get("title", "No Title"),
            "author": ", ".join(volume.get("authors", ["Unknown"])),
            "description": clean_description,
            "image": volume.get("imageLinks", {}).get("thumbnail", "https://via.placeholder.com/150"),
            "categories": ", ".join(volume.get("categories", ["General"])),
            "rating": volume.get("averageRating", "Not Rated"),
            "price": sale.get("listPrice", {}).get("amount"),
            "currency": sale.get("listPrice", {}).get("currencyCode"),
            "saleability": sale.get("saleability", "NOT_FOR_SALE")
        })

    return books


# -------------------------------
# Home Page (Recommendations)
# -------------------------------
@app.route("/")
def home():
    url = f"https://www.googleapis.com/books/v1/volumes?q=bestseller&maxResults=8&key={API_KEY}"
    response = requests.get(url).json()
    books = extract_books(response)
    return render_template("index.html", books=books)


# -------------------------------
# Search
# -------------------------------
@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return home()

    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=12&key={API_KEY}"
    response = requests.get(url).json()
    books = extract_books(response)

    return render_template("index.html", books=books)


# -------------------------------
# Book Details
# -------------------------------
@app.route("/book/<book_id>")
def book_detail(book_id):
    url = f"https://www.googleapis.com/books/v1/volumes/{book_id}?key={API_KEY}"
    response = requests.get(url).json()
    book = extract_books({"items": [response]})[0]
    return render_template("book.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
