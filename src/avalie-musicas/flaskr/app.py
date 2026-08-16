from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy()
db.init_app(app)

from .models import Musica

@app.route("/", methods=["GET", "POST"])
def adicionar_musica():

    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]
        nota = request.form["nota"]
        avaliacao = request.form["avaliacao"]

        musica = Musica(
            titulo = titulo,
            autor = autor,
            nota = nota,
            avaliacao = avaliacao,
        )

        db.session.add(musica)
        db.session.commit()

        return redirect(url_for("musicas"))
    return render_template("index.html")

@app.route("/musicas")
def musicas():
    musicas = db.session.execute( db.select(Musica)).scalars().all()
    return render_template( "musicas.html", musicas=musicas)

@app.route("/musicas/<int:id>/editar", methods=["GET", "POST"])
def editar_musica(id):
    musica = db.get_or_404(Musica, id)
    if request.method == "POST":

        musica.titulo = request.form["titulo"]
        musica.autor = request.form["autor"]
        musica.nota = float(request.form["nota"])
        musica.avaliacao = request.form["avaliacao"]

        db.session.commit()

        return redirect(url_for("musicas"))

    return render_template(
        "editar_musica.html",
        musica=musica
    )

@app.route("/musicas/<int:id>/deletar", methods=["POST"])
def deletar_musica(id):

    print("MÉTODO RECEBIDO:", request.method)

    musica = db.get_or_404(Musica, id)

    db.session.delete(musica)
    db.session.commit()

    return redirect(url_for("musicas"))

with app.app_context():
    db.create_all()
    