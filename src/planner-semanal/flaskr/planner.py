from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('planner', __name__)

afazeres = [{"tarefa":"exemplo", "finalizado": False}]
@bp.route('/')
def index():
    
    return render_template('planner/index.html', afazeres = afazeres)

@bp.route("/add", methods=["POST"])
def add():
    afazer = request.form['afazer']
    afazeres.append({"tarefa": afazer, "finalizado": False})
    return redirect(url_for("index"))

@bp.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    afazer = afazeres[index]
    if request.method == "POST":
        afazer['tarefa'] = request.form["afazer"]
        return redirect(url_for("index"))
    else:
        return render_template("planner/edit.html", afazer=afazer, index=index)

@bp.route("/check/<int:index>")  
def check(index):
    afazeres[index]['finalizado'] = not afazeres[index]['finalizado']
    return redirect(url_for("index"))

@bp.route("/delete/<int:index>")
def delete(index):
    del afazeres[index]
    return redirect(url_for("index"))