from flask import Flask
import sqlite3
import os
from dotenv import load_dotenv
import db

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def conectar():
    conexao=sqlite3.connect('meu_banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

from views import *

if __name__ == '__main__':
    app.run(debug=True)

