from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(60), nullable=False, unique=True)

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Band: ', self.band_name, '\r\n',
        ])


class Venues(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(30), nullable=False, unique=True)
    
    post = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
        'Venue: ', self.venue_name, '\r\n',
        ])


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
