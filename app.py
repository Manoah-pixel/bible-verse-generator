from flask import Flask, render_template
import random
import os

app = Flask(__name__)

verses = [
    "Romans 8:28 - And we know that in all things God works for the good...",
    "John 3:16 - For God so loved the world...",
    "Psalm 23:1 - The Lord is my shepherd, I shall not want.",
    "Proverbs 3:5 - Trust in the Lord with all your heart...",
    "Philippians 4:13 - I can do all things through Christ who strengthens me."
]

@app.route("/", methods=["GET", "POST"])
def index():
    verse = random.choice(verses)
    return render_template("index.html", verse=verse)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
