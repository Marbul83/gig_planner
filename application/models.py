from application import db


class Gigs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db.Column('band_id', db.Integer, db.ForeignKey('bands.band_id')),
    db.Column('venue_id', db.Integer, db.ForeignKey('venues.venue_id'))

class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(60), nullable=False, unique=True)

    #gigplanner = db.relationship('Venues', secondary=gigs, backref=db.backref('gigplanner', lazy= True))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Band: ', self.band_name, '\r\n',
        ])

        
class Venues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(30), nullable=False, unique=True)
    gig = db.relationship('Bands', backref='plan', lazy=True)


    #gigplanner = db.relationship('Venues', secondary=gigs, backref=db.backref('gigplanner', lazy= True))

    def __repr__(self):
        return ''.join([
            'Venue: ', self.venue_name, '\r\n',
        ])


# need to create composite db