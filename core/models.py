# from flask.ext.sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from django.db import models
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/bogdan/PycharmProjects/ARBUZ_back/db.sqlite3'
# db = SQLAlchemy(app)


class Building(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()


class Crimes(models.Model):
    building_id = models.ForeignKey(Building, related_name='building')
    year_month = models.DateField(max_length=8)
    total = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    bodily_harm_with_fatal_cons = models.IntegerField(default=0)
    brigandage = models.IntegerField(default=0)
    drugs = models.IntegerField(default=0)
    extortion = models.IntegerField(default=0)
    fraud = models.IntegerField(default=0)
    grave_and_very_grave = models.IntegerField(default=0)
    hooliganism = models.IntegerField(default=0)
    intentional_injury = models.IntegerField(default=0)
    looting = models.IntegerField(default=0)
    murder = models.IntegerField(default=0)
    rape = models.IntegerField(default=0)
    theft = models.IntegerField(default=0)

#
# class Building(db.Model):
#
#     __tablename__ = 'building'
#
#     id = db.Column(db.Integer, primary_key=True)
#     street = db.Column(db.String(100))
#     number = db.Column(db.Integer)
#     longitude = db.Column(db.Float)
#     latitude = db.Column(db.Float)
#     crimes = db.relationship('Crimes', backref='building', lazy='dynamic')
#
#
# class Crimes(db.Model):
#
#     __tablename__ = 'crimes'
#
#     id = db.Column(db.Integer, primary_key=True)
#     building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
#     year_month = db.Column(db.Date)
#     total = db.Column(db.Integer, default=0)
#     total_points = db.Column(db.Integer, default=0)
#     bodily_harm_with_fatal_cons = db.Column(db.Integer, default=0)
#     brigandage = db.Column(db.Integer, default=0)
#     drugs = db.Column(db.Integer, default=0)
#     extortion = db.Column(db.Integer, default=0)
#     fraud = db.Column(db.Integer, default=0)
#     grave_and_very_grave = db.Column(db.Integer, default=0)
#     hooliganism = db.Column(db.Integer, default=0)
#     intentional_injury = db.Column(db.Integer, default=0)
#     looting = db.Column(db.Integer, default=0)
#     murder = db.Column(db.Integer, default=0)
#     rape = db.Column(db.Integer, default=0)
#     theft = db.Column(db.Integer, default=0)
