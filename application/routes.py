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
		venue_id=request.args.get("venue_id")
		venue=Venues.query.filter_by(id=venue_id).first()
		bandData = Bands(
			band_name=form.band_name.data,
			plan=venue
		)
		db.session.add(bandData)
		db.session.commit()
		return redirect(url_for('planner'))

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
		return redirect(url_for('add_band', venue_id=venueData.id))

	else:
		print(form.errors)
	return render_template('add_venue.html', title='Add Venue', form=form)


@app.route('/planner', methods=['GET', 'POST'])
def planner():
	bandData = Bands.query.all()

	return render_template('planner.html', title='Gig Planner', bands=bandData)

@app.route("/planner/delete", methods=["GET", "POST"])
def plan_delete():
        posts = Posts.query.filter_by(user_id=user)
        for post in posts:
                db.session.delete(post)
        account = Users.query.filter_by(id=user).first()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for('register'))


