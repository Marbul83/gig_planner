from application import db


class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(60), nullable=False, unique=True)

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Band: ', self.band_name, '\r\n',
        ])


class Venues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(30), nullable=False, unique=True)
    
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'), nullable=False)
    #post = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['Venue: ', self.venue_name, '\r\n',
        ])


# need to create composite db