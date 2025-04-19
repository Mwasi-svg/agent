import google.generativeai as genai

# Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyDd5bDQUz5hTC8rNOYEKjfUsPPzpRbN1iI")

# List of available models to confirm
available_models=[m.name for m in genai.list_models()]
print("Available models:", available_models)

#Load Gemini 1.5 Model if available
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
""")


print("🧠 Gemini Chat — type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:
        response = model.generate_content(user_input)
        print("Gemini:", response.text, "\n")
    except Exception as e:
        print("❌ Error:", e)
