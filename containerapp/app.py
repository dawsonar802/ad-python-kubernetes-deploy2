from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def frogs():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='52.162.89.227', port='80')
