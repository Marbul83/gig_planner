from application import db
from application.models import Bands, Venues


db.drop_all()
db.create_all()