from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os 

load_dotenv()

app = Flask(__name__)

# 🔐 Put your token here
IK_TOKEN = os.getenv("Indian-Kanoon-Api-Key")

BASE_URL = "https://api.indiankanoon.org"

HEADERS = {
    "Authorization": f"Token {IK_TOKEN}"
}

def search_cases(query):
    url = f"{BASE_URL}/search/"
    
    data = {
        "formInput": query,
        "pagenum": 0
    }

    response = requests.post(url, headers=HEADERS, data=data, timeout=30)
    response.raise_for_status()
    return response.json()

def get_document(docid):
    url = f"{BASE_URL}/doc/{docid}/"
    response = requests.post(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    document = None

    if request.method == "POST":
        if "search_query" in request.form:
            query = request.form["search_query"]
            results = search_cases(query)

    return render_template("index.html", results=results, document=document)

@app.route("/api/document/<docid>", methods=["GET"])
def get_doc_details(docid):
    """Fetch full document details from Indian Kanoon API"""
    try:
        doc_data = get_document(docid)
        return jsonify(doc_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)