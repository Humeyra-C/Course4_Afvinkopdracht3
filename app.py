"""
Author: Humeyra Copoglu
Date: 25-04-2022
Content: BIN-1a OWE4 Afvinkopdracht 3B
"""
from flask import Flask
import mysql_connect as db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    connect = db
    if connect.success:
        return 'Hello World!'
    else:
        return 'Connection failed!'


if __name__ == '__main__':
    app.run()


