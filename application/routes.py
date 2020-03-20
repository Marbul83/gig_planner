from application import app, db
from flask import render_template, redirect, url_for, request
from application.forms import BandForm, VenueForm
from application.models import Bands, Venues


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/add_band', methods=['GET', 'POST'])
def add_band():
	form = BandForm()
	if form.validate_on_submit():
		bandData = Bands(
			band_name=form.band_name.data
		)
		db.session.add(bandData)
		db.session.commit()
		return redirect(url_for('add_venue'))

	else:
		print(form.errors)
	return render_template('add_band.html', title='Add Band', form=form)


@app.route('/add_venue', methods=['GET', 'POST'])
def add_venue():
	form = VenueForm()
	if form.validate_on_submit():
		venueData = Venues(
			venue_name=form.venue_name.data
		)
		db.session.add(venueData)
		db.session.commit()
		return redirect(url_for('planner'))

	else:
		print(form.errors)
	return render_template('add_venue.html', title='Add Venue', form=form)


@app.route('/planner', methods=['GET', 'POST'])
def planner():

	# Query gigs table for band_id and venue_id set variables
	# loop through all gigs
	# 	bandData = Bands.query.filter_by(band_id=bandVariable).first()
	# 	same for venue
	#	add band name and venue name to a list
	# pass list to planner

	return render_template('planner.html', title='Gig Planner', add_band=bandData)





#route for planner page needs to have a render template to two tables
#that queries the two tables to pull up the results to add to planner page

