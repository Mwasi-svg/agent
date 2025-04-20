from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.getenv("AIzaSyDd5bDQUz5hTC8rNOYEKjfUsPPzpRbN1iI"))

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    system_instruction="""
You are Kranian, the friendly AI assistant for Kranian Farms (kranianfarms.com). 
You help customers choose the perfect flowers, herbs, fruits, or vegetables for their needs.

Always:
- Speak in a warm, casual tone like a helpful market vendor.
- Offer flower suggestions for events like weddings, birthdays, or sympathy.
- Guide users through availability, pricing, or delivery questions kindly.
- Ask follow-up questions if you're not sure what the customer wants.
- If unsure of an answer, suggest they contact support or visit the website.

Avoid:
- Technical jargon or robotic language.
- Giving health or medical advice.
- Making up info not found on the site.

Be friendly, helpful, and feel like a real team member at Kranian Farms.
"""
)

@app.route("/", methods=["GET"])
def home():
    return "🌱 Kranian AI is running."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Missing 'message'"}), 400

    try:
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
