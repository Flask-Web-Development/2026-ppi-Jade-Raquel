from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy()
db.init_app(app)

from models import Musica

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

        return "Música adicionado com sucesso!"

    with app.app_context():
        db.create_all()
        
    return render_template("index.html")
    