# chatgpt_flask/app/routes.py

from flask import Blueprint, render_template, request, jsonify
import openai
import os

main = Blueprint('main', __name__)

# Load the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150  # Adjust the max_tokens as per your requirements
        )
        chat_response = response.choices[0].message['content'].strip()
        return jsonify({'response': chat_response})
    except Exception as e:
        print(f"Error: {e}")  # Print the error to the console for debugging
        return jsonify({'error': str(e)}), 500
