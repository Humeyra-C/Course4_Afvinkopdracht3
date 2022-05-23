"""
Author: Humeyra Copoglu
Date: 25-04-2022
Content: BIN-1a OWE4 Afvinkopdracht 3B
"""
from flask import Flask, render_template, request, redirect
import mysql.connector as sql

app = Flask(__name__)
connection = False


def ebcra_connect(user, password):
    try:
        global connection
        connection = sql.connect(host='145.74.104.145',
                                 user=user,
                                 password=password,
                                 db='ebcra')
    except Exception as e:
        print("Caught exception: ", e)
        connection = False
        return False
    else:
        return True


@app.route('/', methods=["POST", "GET"])
def index():
    return redirect("/login.html")


@app.route('/login.html', methods=["POST", "GET"])
def login():  # put application's code here
    if request.method == "POST":
        user = request.form.get("Gebruiksnaam", "")
        password = request.form.get("Wachtwoord", "")
        if ebcra_connect(user, password):
            return redirect("/studenten.html")
        else:
            return render_template("login.html", error="Uw gebruiksnaam of wachtwoord klopt niet!")
    else:
        return render_template("login.html")


@app.route('/studenten.html', methods=["POST", "GET"])
def student():
    global connection
    if connection:
        cursor = connection.cursor()
        if request.method == "POST":
            if request.form['knop'] == "Wis filter":
                return redirect("/studenten.html")
            else:
                target = request.form.get("zoeken", "")
                target = "%" + target + "%"
                cursor.execute("SELECT * from student "
                               "WHERE student_nr LIKE %s "
                               "OR voornaam LIKE %s "
                               "OR achternaam LIKE %s "
                               "OR tussenvoegsels LIKE %s "
                               "OR achternaam LIKE %s "
                               "OR geb_datum LIKE %s "
                               "OR woonplaats LIKE %s "
                               "OR email LIKE %s "
                               "OR mobiel LIKE %s "
                               "OR klas_id LIKE %s "
                               "OR slb_id LIKE %s ",
                               (target, target, target, target, target, target, target, target, target, target, target))
                studenten = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                studenten.insert(0, column_names)
                return render_template("studenten.html", studenten=studenten)
        else:
            cursor.execute("SELECT * from student ")
            studenten = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            studenten.insert(0, column_names)
            return render_template("studenten.html", studenten=studenten)
    else:
        return redirect("/login.html")


if __name__ == '__main__':
    app.run()
