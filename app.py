from flask import Flask, render_template, request, redirect
from accountant import magazyn, saldo, magazyn_func, przeglad_func, historia_operacji, zapis_do_pliku
from manager import Manager

app = Flask(__name__)
manager = Manager("in.txt")


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":        # TODO: jak zapisać dane z formularza?
        if request.form["nazwa"] == "sprzedaz":
            name = request.form["name2"]
            price = request.form["price2"]
            amount = request.form["amount2"]
            polecenie = ("sprzedaz", name, price, amount)
            manager.sprzedaz_func(polecenie)
            manager.historia_operacji.append(polecenie)
            manager.zapis_do_pliku()
        return redirect("/")
    return render_template("main.html", magazyn=manager.magazyn, saldo=manager.saldo)   # TODO: dlaczego saldo się nie wczytuje, a magazyn już tak?


@app.route('/historia/')  # , methods=['POST'])     # TODO:wielokrotne dodawanie historii, jak dodać POST?
def historia():
    przeglad_func()
    return render_template("historia.html", historia_operacji=historia_operacji)


@app.route('/historia/<line_from>/<line_to>/')
def historia_przedzial(line_from, line_to):
    przeglad_func()
    historia_czesc = historia_operacji[int(line_from):int(line_to) + 1]
    return render_template("historia_przedzial.html",
                           historia_czesc=historia_czesc, line_from=line_from, line_to=line_to)




