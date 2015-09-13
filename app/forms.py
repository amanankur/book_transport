__author__ = 'amanankur'

from flask.ext.wtf import Form
from wtforms import StringField, TextField, SubmitField,BooleanField, TextAreaField, SelectField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired, Length


class AddDriverForm(Form):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    contact = StringField('contact')
    vehicleNum = StringField('vechicleNum')
    submit = SubmitField("AddDriver")

# ["Name", "PhoneNumber", "StartLocation", "EndLocation", "driver"]
class AddBookingForm(Form):
    name = StringField('name')
    phoneNum = StringField('phoneNum')
    startLoc = StringField('startLoc')
    endLoc = StringField('endLoc')
    submit = SubmitField("AddBooking")

class EditForm(Form):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    contact = StringField('contact')
    vehicleNum = StringField('vechicleNum')
    name = StringField('name')
    phoneNum = StringField('phoneNum')
    startLoc = StringField('startLoc')
    endLoc = StringField('endLoc')

class AssignForm(Form):
    booking_type = SelectField(u'Booking Name List')
    driver_type = SelectField(u'Driver Name List')

