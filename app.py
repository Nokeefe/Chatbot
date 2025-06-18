from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyBu4cBQ_DC7tj-OcexuJHppAMNUjK4Oe08")  # Use a secure method in production

# Use Gemini model (correct latest name)
model = genai.GenerativeModel("gemini-1.5-flash")  # Remove "models/" prefix

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

        # Generate Gemini response
        response = model.generate_content(prompt)

        return jsonify({"reply": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/test")
def test():
    return jsonify({"status": "Flask working and Gemini model loaded"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
