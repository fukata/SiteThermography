# -*- coding: utf-8 -*-
# thermography.models

from google.appengine.ext import db
import admin.models

# Create your models here.
class Thermographies(db.Model):
	data = db.TextProperty()
	calculate_status = db.IntegerProperty()
	url = db.LinkProperty()
	site = db.ReferenceProperty(admin.models.Sites)

class ThermographyPoints(db.Model):
	thermography = db.ReferenceProperty(Thermographies)
	site = db.ReferenceProperty(admin.models.Sites)
	url = db.LinkProperty()
	data = db.TextProperty()
	year_calculate_status = db.IntegerProperty()
	month_calculate_status = db.IntegerProperty()
	day_calculate_status = db.IntegerProperty()
	date = db.StringProperty() # YYYYMMDD
	year = db.IntegerProperty() # YYYY
	month = db.IntegerProperty() # MM
	day = db.IntegerProperty() # DD

class ThermographyPointDaily(db.Model):
	site = db.ReferenceProperty(admin.models.Sites)
	url = db.LinkProperty()
	data = db.TextProperty()
	calculate_status = db.IntegerProperty()
	date = db.StringProperty() # YYYYMMDD
	year = db.IntegerProperty() # YYYY
	month = db.IntegerProperty() # MM
	day = db.IntegerProperty() # DD
	max_point = db.IntegerProperty()
	
	@property
	def display_date(self):
		if int(self.month) == 0 and int(self.day) == 0:
			return self.year
		elif int(self.day) == 0:
			return "%d/%02d" % (self.year, self.month)
		else:
			return "%d/%02d/%02d" % (self.year, self.month, self.day)
			
