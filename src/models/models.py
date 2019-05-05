from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)

    def __ref__(self):
        return '<user %r>'.format(self.username)

