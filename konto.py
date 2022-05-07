from app import dotychczasowa_historia_operacji
from app import historia_na_dzialania
from app import manager
from flask import Flask, render_template


manager.execute("konto")

app = Flask(__name__)


@app.route('/')
# @manager.assign("konto")
def konto_func():  # (abc):
    dotychczasowa_historia_operacji()
    saldo = historia_na_dzialania()[0]
    return render_template("main.html", saldo=saldo)

