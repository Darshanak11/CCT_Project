from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

scores = {'user': 0, 'computer': 0, 'draws': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html', user_score=scores['user'], computer_score=scores['computer'], draws=scores['draws'])

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "draw"
        scores['draws'] += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "win"
        scores['user'] += 1
    else:
        result = "lose"
        scores['computer'] += 1

    return jsonify({'result': result, 'computer_choice': computer_choice})

@app.route('/reset', methods=['POST'])
def reset():
    scores['user'] = 0
    scores['computer'] = 0
    scores['draws'] = 0
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
