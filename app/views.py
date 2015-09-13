from flask import jsonify,render_template, abort, make_response, flash, redirect, session, url_for, request
from app import app, db
from .models import Driver, Booking
from.forms import AddDriverForm, EditForm, AddBookingForm, AssignForm


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html',
                           title='Home'
                           )


# Method to get the list of all the drivers available.
@app.route('/transport/drivers', methods = ['GET', 'POST'])
def get_drivers():

    form = AddDriverForm()

    driver_all = Driver.query.all()

    if request.method == 'POST':

        if request.form['submit'] == 'Add Driver':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            contact = request.form['contact']
            vehicle_no = request.form['vehicleNum']

            add_driver = Driver(first_name = first_name, last_name = last_name, contact = contact, vehicleNum = vehicle_no)
            db.session.add(add_driver)
            db.session.commit()
            flash('New Driver has been added.')
            return redirect(url_for('get_drivers'))



    return render_template('driver_list.html',
                           title='Home',
                           driver_list = driver_all,
                           form = form
                           )

# Method to get the details of one driver.
@app.route('/transport/drivers/<driver_id>', methods = ['GET'])
def get_driver(driver_id):
    driver_detail = Driver.query.filter_by(id = driver_id).first()


    return render_template('driver_detail.html',
                           title='Home',
                           driver_details = driver_detail,
                           #form = form
                           )

# Method to edit the details of a driver.
@app.route('/transport/drivers/edit/<driver_id>', methods=['GET','POST'])
def edit(driver_id):
    form = EditForm()
    driver_detail = Driver.query.filter_by(id = driver_id).first()

    if request.method == 'POST':
        if form.validate_on_submit():
            if form.first_name.data:
                driver_detail.first_name = form.first_name.data
            if form.last_name.data:
                driver_detail.last_name = form.last_name.data
            if form.contact.data:
                driver_detail.contact = form.contact.data
            if form.vehicleNum.data:
                driver_detail.vehicleNum = form.vehicleNum.data

            db.session.add(driver_detail)
            db.session.commit()
            flash('Your changes have been saved.')

            return redirect(url_for('get_driver', driver_id = driver_detail.id))
    else:
        return render_template('edit.html', form=form)


# Method to get details of all the bookings available.
@app.route('/transport/bookings', methods = ['GET', 'POST'])
def get_bookings():

    form = AddBookingForm()

    booking_all = Booking.query.all()

    if request.method == 'POST':

        if request.form['submit'] == 'Add Booking':
            name = request.form['name']
            phoneNum = request.form['phoneNum']
            startLoc = request.form['startLoc']
            endLoc = request.form['endLoc']

            add_booking = Booking(name = name, phoneNum = phoneNum, startLoc = startLoc, endLoc = endLoc)
            db.session.add(add_booking)
            db.session.commit()
            flash('New Booking has been added.')
            return redirect(url_for('get_bookings'))



    return render_template('booking_list.html',
                           title='Home',
                           booking_list = booking_all,
                           form = form
                           )


# Method to get the details of a booking.
@app.route('/transport/bookings/<booking_id>', methods = ['GET'])
def get_booking(booking_id):
    booking_detail = Booking.query.filter_by(id = booking_id).first()


    return render_template('booking_detail.html',
                           title='Home',
                           booking_details = booking_detail,
                           #form = form
                           )

# Method to edit details of a booking.
@app.route('/transport/bookings/edit/<booking_id>', methods=['GET','POST'])
def book_edit(booking_id):
    form = EditForm()
    booking_detail = Booking.query.filter_by(id = booking_id).first()

    if request.method == 'POST':
        if form.validate_on_submit():
            if form.name.data:
                booking_detail.name = form.name.data
            if form.phoneNum.data:
                booking_detail.phoneNum = form.phoneNum.data
            if form.startLoc.data:
                booking_detail.startLoc = form.startLoc.data
            if form.endLoc.data:
                booking_detail.endLoc = form.endLoc.data

            db.session.add(booking_detail)
            db.session.commit()
            flash('Your changes have been saved.')

            return redirect(url_for('get_booking', booking_id = booking_detail.id))
    else:
        return render_template('edit_book.html', form=form)


# Method to assign a Driver to a Booking
@app.route('/transport/assign', methods = ['GET', 'POST'])
def assign_driver():

    form = AssignForm()

    booking_all = Booking.query.all()
    driver_all = Driver.query.all()
    form.booking_type.choices = [(book.id, book.name) for book in booking_all]
    form.driver_type.choices = [(driver.id, driver.first_name) for driver in driver_all]

    if request.method == 'POST':
        booking_id = request.form['booking_type']
        booking_detail = Booking.query.filter_by(id = booking_id).first()

        driver_id = request.form['driver_type']
        driver_detail = Driver.query.filter_by(id = driver_id).first()

        booking_detail.driver = driver_detail
        db.session.commit()

        flash('Your changes have been saved.')

        return redirect(url_for('assign_driver'))



    return render_template('assign_driver.html',
                           title='Home',
                           #booking_details = booking_detail,
                           form = form
                           )

# Method to delete a booking.
@app.route('/transport/bookings/delete/<booking_id>', methods=['POST'])
def delete_booking(booking_id):
    if request.method =='POST':
        booking = Booking.query.filter_by(id = booking_id).first()
        db.session.delete(booking)
        db.session.commit()
        flash('Booking Deleted')
        return redirect(url_for('get_bookings'))

#Method to delete a Driver
@app.route('/transport/drivers/delete/<driver_id>', methods=['POST'])
def delete_driver(driver_id):
    if request.method =='POST':
        driver = Driver.query.filter_by(id = driver_id).first()
        db.session.delete(driver)
        db.session.commit()
        flash('Driver Deleted')
        return redirect(url_for('get_drivers'))
