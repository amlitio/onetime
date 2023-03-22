from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

model_engine = "text-davinci-002"

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user-input']
    bot_response = ask_gpt(user_input)
    return jsonify({'response': bot_response})
