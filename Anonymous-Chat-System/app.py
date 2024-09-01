from flask import Flask, render_template, request, jsonify, session
import json
import os
import random
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DB_PATH = 'messages-info/database.json'

def read_messages():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def write_message(message):
    messages = read_messages()
    messages.append(message)
    with open(DB_PATH, 'w') as f:
        json.dump(messages, f)

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def get_user_color():
    if 'color' not in session:
        session['color'] = generate_random_color()
    return session['color']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(read_messages())

@app.route('/messages', methods=['POST'])
def post_message():
    message = request.json.get('message')
    if message:
        color = get_user_color()
        write_message({'message': message, 'color': color})
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)


