from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

points = 0

mole_x = random.randint(0, 1400) 
mole_y = random.randint(300, 500) 

@app.route('/')
def index():
    return render_template('index.html', points=points, mole_x=mole_x, mole_y=mole_y)

@app.route('/point', methods=['POST'])
def point():
    global points, mole_x, mole_y
    points += 1
    if points >= 15:
        return redirect(url_for('win'))
    else:
        mole_x = random.randint(0, 1400) 
        mole_y = random.randint(300, 500) 
        return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    global points, mole_x, mole_y
    points = 0
    mole_x = random.randint(0, 1400)  
    mole_y = random.randint(300, 500) 
    return redirect(url_for('index'))

@app.route('/play-again', methods=['GET'])
def play_again():
    global points, mole_x, mole_y
    points = 0
    mole_x = random.randint(0, 1400)  
    mole_y = random.randint(300, 500)  
    return redirect(url_for('index'))

@app.route('/win')
def win():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
