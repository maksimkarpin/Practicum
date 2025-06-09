from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def lesson1():
    return render_template('index1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
