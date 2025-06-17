from enum import unique

from flask import Flask, render_template, request, redirect ,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diary.db"
db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app, db)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(80), unique=True, nullable = False)
    subtitle = db.Column(db.String)
    text = db.Column(db.Text, nullable=False)

@app.route('/lesson4',methods=["POST"])
def lesson4():
    notes = Note.query.all()
    note = Note(heading=request.form['heading'], subtitle=request.form['subtitle'], text=request.form['text'])
    db.session.add(note)
    db.session.commit()
    for note in notes:
        id = note.id
        heading = note.heading
        subtitle = note.subtitle
        text = note.text
    return render_template('index4.html', heading=heading, text=text, subtitle=subtitle)

@app.route('/create4')
def create4():
    #note = Note(heading=request.form['heading'], subtitle=request.form['subtitle'], text=request.form['text'])
    #db.session.add(note)
    #db.session.commit()
    return render_template('note4.html')



@app.route('/lesson4_add')
def lesson4_add():

    #note = Note(heading=request.form['heading'], subtitle=request.form['subtitle'], text=request.form['text'])
    #db.session.add(note)
    #db.session.commit()
    return url_for('index4')



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




@app.route('/create')
def create():
    return render_template('note.html')







if __name__ == '__main__':
    app.run(debug=True)
