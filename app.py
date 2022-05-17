from flask import Flask, render_template, request, redirect
from manager import Manager

app = Flask(__name__)
manager = Manager("in.txt")


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        if request.form["operacja"] == "sprzedaz":
            name = request.form["name2"]
            price = request.form["price2"]
            amount = request.form["amount2"]
            polecenie = ("sprzedaz", name, price, amount)
            manager.sprzedaz_func(polecenie)
        elif request.form["operacja"] == "zakup":
            name = request.form["name1"]
            price = request.form["price1"]
            amount = request.form["amount1"]
            polecenie = ("zakup", name, price, amount)
            manager.zakup_func(polecenie)
        elif request.form["operacja"] == "saldo":
            name = request.form["name3"]
            price = request.form["price3"]
            polecenie = ("saldo", price, name)
            manager.saldo_func(polecenie)
        manager.historia_operacji.append(polecenie)
        if manager.error == 0:
            manager.zapis_do_pliku()
        else:
            return redirect('/error/')
        return redirect('/')
    return render_template("main.html", magazyn=manager.magazyn, saldo=manager.saldo)


@app.route('/error/')
def error():
    return render_template("error.html"), {"Refresh": "4; url=/"}


@app.route('/historia/')
def historia():
    return render_template("historia.html", historia_operacji=manager.historia_operacji)


@app.route('/historia/<line_from>/<line_to>/')
def historia_przedzial(line_from, line_to):
    historia_czesc = manager.historia_operacji[int(line_from):int(line_to) + 1]
    return render_template("historia_przedzial.html",
                           historia_czesc=historia_czesc, line_from=line_from, line_to=line_to)
