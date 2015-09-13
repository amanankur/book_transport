__author__ = 'amanankur'
from app import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    contact = db.Column(db.String(120), index=True, unique=True)
    vehicleNum = db.Column(db.String(120), index=True, unique=True)
    book = db.relationship('Booking', backref = 'driver', lazy ='dynamic')


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    phoneNum = db.Column(db.String(120), index=True, unique=True)
    startLoc = db.Column(db.String(120), index=True, unique=True)
    endLoc = db.Column(db.String(120), index=True, unique=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))



