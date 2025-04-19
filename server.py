from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyDd5bDQUz5hTC8rNOYEKjfUsPPzpRbN1iI")

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    system_instruction="""
You are Kranian, the helpful and friendly AI assistant for kranianfarms.com.
Answer customer questions casually, informatively, and clearly.
"""
)

app = Flask(__name__)
CORS(app)  # So frontend can connect

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = model.generate_content(user_message)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(port=5000)
