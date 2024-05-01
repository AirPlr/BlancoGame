from flask import Flask, request, render_template
import random

app = Flask(__name__)

players = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        ip = request.remote_addr
        word = players.get(ip, {}).get('word', '')
        players[ip] = {'name': name, 'word': word}
        return render_template('game.html', word=word)
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', players=players)

@app.route('/start', methods=['POST'])
def start_game():
    word = request.form['word']
    for player in players.values():
        player['word'] = word
    blanco_player = random.choice(list(players.values()))
    blanco_player['word'] = "Blanco"
    return render_template('admin.html', players=players)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)