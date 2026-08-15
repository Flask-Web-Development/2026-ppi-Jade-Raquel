from app import db
from datetime import datetime

class Musica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    nota = db.Column(db.Float(10))
    avaliacao = db.Column(db.Text(500), nullable=False)
    data_publicacao = db.Column(db.Date,default=datetime.now, nullable=False)
