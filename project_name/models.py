from project_name import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(150), nullable = False)
