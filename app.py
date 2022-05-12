from flask import Flask, render_template
from accountant import magazyn, saldo, magazyn_func, przeglad_func, historia_operacji

app = Flask(__name__)


@app.route('/')
def main():
    magazyn_func()
    # print(magazyn)
    return render_template("main.html", magazyn=magazyn, saldo=saldo)


@app.route('/historia/')
def historia():
    przeglad_func()
    return render_template("historia.html", historia_operacji=historia_operacji)

@app.route('/historia/<line_from>/<line_to>/')
def historia_przedzial():
    przeglad_func()




