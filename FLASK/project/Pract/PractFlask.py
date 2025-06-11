from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def lesson1():
    return render_template('index1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('index2.html')

@app.route('/lesson3/st')
def lesson3st():
    return render_template('notes.html')

@app.route('/lesson3' , methods=["POST"])
def lesson3():
    heading = request.form["heading"]
    text = request.form["text"]
    note = {}
    note.clear()
    new_note = {heading: text}
    note.update(new_note)
    for tx in note:
        t = tx
    return render_template('notes.html',t=t,note=note.get(heading))

@app.route('/cart')


@app.route('/create')
def create():
    return render_template('note.html')







if __name__ == '__main__':
    app.run(debug=True)
