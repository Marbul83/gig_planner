from application import db



<<<<<<< HEAD
gigs = db.Table ('gigs',
=======
gigs = db.Table('gigs',
>>>>>>> development
    db.Column('band_id', db.Integer, db.ForeignKey('Bands.band_id')),
    db.Column('venue_id', db.Integer, db.ForeignKey('Venues.venue_id'))
    )

class Bands(db.Model):
    band_id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(60), nullable=False, unique=True)

<<<<<<< HEAD
    gigplanner = db.relationships('Venues', secondary=gigs, backref=db.backref('gigplanner', lazy= True))
   
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
=======
   gigplanner = db.relationships('Venues', secondary=gigs, backref=db.backref('gigplanner', lazy= True))
   
   venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
>>>>>>> development

    def __repr__(self):
        return ''.join([
            'Band: ', self.band_name, '\r\n',
        ])


class Venues(db.Model):
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(30), nullable=False, unique=True)
    
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'), nullable=False)

    def __repr__(self):
        return ''.join(['Venue: ', self.venue_name, '\r\n',
        ])


# need to create composite db