from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key directly here or from environment
genai.configure(api_key="AIzaSyBu4cBQ_DC7tj-OcexuJHppAMNUjK4Oe08")  # Replace with actual key

# Create the model
model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        prompt = data.get("message", "")

        if not prompt:
            return jsonify({"error": "No input"}), 400

        # Send prompt to Gemini
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
