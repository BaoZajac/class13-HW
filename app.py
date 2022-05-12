from flask import Flask, render_template
from accountant import magazyn, saldo, magazyn_func, przeglad_func, historia_operacji

app = Flask(__name__)


@app.route('/')
def main():
    magazyn_func()
    # print(magazyn)
    return render_template("main.html", magazyn=magazyn, saldo=saldo)   #TODO: dlaczego saldo się nie wczytuje, a magazyn już tak?


@app.route('/historia/')  # , methods=['POST'])     #TODO:wielokrotne dodawanie historii, jak dodać POST?
def historia():
    przeglad_func()
    return render_template("historia.html", historia_operacji=historia_operacji)


@app.route('/historia/<line_from>/<line_to>/')
def historia_przedzial(line_from, line_to):
    przeglad_func()
    historia_czesc = historia_operacji[int(line_from):int(line_to) + 1]
    return render_template("historia_przedzial.html",
                           historia_czesc=historia_czesc, line_from=line_from, line_to=line_to)




