from flask import Flask, render_template, request
import sqlite3
import os

from sqlalchemy import null

currentDirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/enternew")
def new_student():
    return render_template("student.html")


@app.route("/addrec", methods=['POST', "GET"])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form["nm"]
            addr = request.form["add"]
            city = request.form["city"]
            pin = request.form["pin"]
            with sqlite3.connect(currentDirectory + "\phonebook.db") as con:
                cursor = con.cursor()
                cursor.execute(
                    "INSERT INTO students (name,addr,city,pin) VALUES(?,?,?,?)", (nm, addr, city, pin))
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route("/list")
def list():
    con = sqlite3.connect(currentDirectory + "\phonebook.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    cursor.execute("SELECT * from students")
    rows = cursor.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.debug = True
    app.run()
