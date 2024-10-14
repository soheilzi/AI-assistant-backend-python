from flask import Flask, request, jsonify
import openai
from openai import OpenAI
from flask_cors import CORS
import os
# import dotenv
import re

def sanitize_message(message):
    # Remove any special characters, limit length, etc.
    message = re.sub(r'[^\w\s]', ' ', message)  # Basic sanitization (removes non-word characters)
    return message[-1000:]  # Limit input to 1000 characters for safety

# dotenv.load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
app = Flask(__name__)
CORS(app)


# Simple route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    user_message = sanitize_message(user_message)
    # we only care about the last 1000 characters
    print("User message:", user_message)
    
    # GPT response
    response_message = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": user_message
            }
        ]
    ).choices[0].message.content
    
    return jsonify({"response": response_message})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)