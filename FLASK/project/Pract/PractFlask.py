from enum import unique

from flask import Flask, render_template, request, redirect ,url_for, flash, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diary.db"
db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app, db)
app.config["SECRET_KEY"] = 'maxitron'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(80), unique=True, nullable = False)
    subtitle = db.Column(db.String)
    text = db.Column(db.Text, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable = False )
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(50))

@app.route('/home')
def home():
    return render_template( 'home.html')

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        user = Users(request.form["username"], request.form['email'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Пользователь успешно зарегистрирован!')
        return url_for(render_template('login'))

@app.route('/login',  methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = Users.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            token = user.token
            global expiration
            expiration = datetime.now(timezone.utc) + timedelta(minutes=30)
            session['token'] = token
            return url_for('home')
        else:
            flash("Неверные данные!")
            return render_template('home.html')

@app.before_request
def check_auth():
    token = session.get('token')
    if not token or datetime.now(timezone.utc) > expiration:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('home'))

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index4.html'))
    response.set_cookie('username', "Maksim Karpin")
    return response

@app.route('/login/')
def login1():
    session['username'] = "Maksim Karpin"
    return "Вы успешно вошли в систему!"

@app.route('/welcome')
def welcome():
    username = request.cookies.get('username', None)
    #username = session.get('username', None)
    if username is not None:
        return f"{username} вы успешно вошли в систему!"
    else:
        return "Вы не залогинились!"



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
