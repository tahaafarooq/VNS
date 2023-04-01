from flask import Flask, request, render_template, redirect
from model import db, Users, Messages
import africastalking
import random
import sqlite3


africastalking.initialize(
    username="sandbox",
    api_key="56a87b5eaa3998961718b260547d3963691074bc8be340a335db8918bc9aa18a"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


DATABASE = {
    'drivername': 'sqlite',
    'database': 'database.db'
}

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() # create tables in the DB
    # con = sqlite3.connect('database.db')


@app.route('/')
def index():



    return render_template('index.html')


@app.route('/add-recipient', methods=['POST', 'GET'])
def add_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    number = request.form.get('number')

    if number is not None:
        id = random.randint(1,1999)
        user = Users(id=id, first_name=fname, last_name=lname, number=number)
        db.session.add(user)
        db.session.commit()

        return "Created User"

    return "User Can't Be Created"


@app.route('/send-bulk', methods=['GET', 'POST'])
def send_notificaiton():
    if request.method == "POST":
        message = request.form.get('message')
        con = sqlite3.connect('instance/database.db')
        cursor = con.cursor()
        db = cursor.execute("SELECT number FROM users;").fetchall()
        num = len(db)

        phone = []

        for i in range(0,num):
            phone.append(db[i][0])

        sender = "11243"

        try:
            sms = africastalking.SMS
            response = sms.send(message, phone, sender)
            return response
        except Exception as e:
            print(e)
            return f"{e}"
    elif request.method == "GET":
        return render_template('send.html')


if __name__ == '__main__':
    app.run(debug=True)