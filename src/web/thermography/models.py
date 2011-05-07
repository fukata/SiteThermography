# -*- coding: utf-8 -*-
# thermography.models

from google.appengine.ext import db

# Create your models here.
class Thermographies(db.Model):
	data = db.TextProperty()
	calculate_status = db.IntegerProperty()
	url = db.TextProperty()

class ThermographyPoints(db.Model):
	thermography = db.ReferenceProperty(Thermographies)
	data = db.TextProperty()
	year_calculate_status = db.IntegerProperty()
	month_calculate_status = db.IntegerProperty()
	day_calculate_status = db.IntegerProperty()
	date = db.StringProperty() # YYYYMMDD
	year = db.IntegerProperty() # YYYY
	month = db.IntegerProperty() # MM
	day = db.IntegerProperty() # DD
	url = db.TextProperty()

class ThermographyPointDaily(db.Model):
	data = db.TextProperty()
	calculate_status = db.IntegerProperty()
	date = db.StringProperty() # YYYYMMDD
	year = db.IntegerProperty() # YYYY
	month = db.IntegerProperty() # MM
	day = db.IntegerProperty() # DD
	url = db.TextProperty()
	maxPoint = db.IntegerProperty()
