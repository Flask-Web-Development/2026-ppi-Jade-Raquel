from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('planner', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    afazeres = db.execute("""SELECT * FROM task WHERE author_id = ?""",(g.user["id"],)).fetchall()
    return render_template(
    "planner/index.html",
    afazeres=afazeres
)

@bp.route("/add", methods=["POST"])
@login_required
def add():
    db = get_db()
    db.execute( """ INSERT INTO task (author_id, tarefa, dia) VALUES (?, ?, ?) """,
    (g.user["id"],request.form["afazer"],request.form["dia"])
    )
    db.commit()
    return redirect(url_for("planner.index"))

@bp.route("/edit/<int:index>", methods=("GET", "POST"))
@login_required
def edit(index):
    db = get_db()
    afazer = db.execute("""SELECT *FROM task WHERE id = ? AND author_id = ? """,
        (index, g.user["id"])
    ).fetchone()
    if afazer is None:
        abort(404)
    if request.method == "POST":
        db.execute(""" UPDATE task SET tarefa = ?, dia = ? WHERE id = ? AND author_id = ? """,
            (request.form["afazer"],request.form["dia"],index,g.user["id"])
        )
        db.commit()
        return redirect(url_for("planner.index"))
    
    return render_template("planner/edit.html",afazer=afazer,index=index)

@bp.route("/check/<int:index>")
@login_required
def check(index):
    db = get_db()
    db.execute(""" UPDATE task SET finalizado = ? WHERE id = ? AND author_id = ? """,
    (1, index,g.user["id"])
    )
    db.commit()
    return redirect(url_for("planner.index"))

@bp.route("/delete/<int:index>")
@login_required
def delete(index):
    db = get_db()
    db.execute("""DELETE FROM task WHERE id = ? AND author_id = ? """,
    (index, g.user["id"])
    )
    db.commit()
    return redirect(url_for("planner.index"))