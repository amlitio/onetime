from flask import Flask, request, jsonify, render_template
from transformers import pipeline, set_seed

app = Flask(__name__)
chatbot = pipeline('text2text-generation', model='EleutherAI/gpt-neo-2.7B')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.form['user-input']
    set_seed(42)
    chatbot_output = chatbot(user_input, max_length=1000, do_sample=True, temperature=0.7)[0]['generated_text']
    return jsonify({'response': chatbot_output})

if __name__ == '__main__':
    app.run(debug=True)
