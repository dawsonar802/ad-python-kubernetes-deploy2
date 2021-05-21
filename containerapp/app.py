from flask import Flask, render_template


app = Flask(__name__)

@app.route('/frogs', methods=['GET'])

def pups():
    return render_template('index.html')
