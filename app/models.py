from . import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    # password_hash = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # pitches = db.relationship('Pitch', backref='user', lazy="dynamic")

    # @property
    # def password(self):
    #     raise AttributeError('You cannnot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    # def save_user(self):
    #     db.session.add(self)
    #     db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

