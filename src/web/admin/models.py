# -*- coding: utf-8 -*-
# admin.models

from google.appengine.ext import db
from kay.auth.models import GoogleUser

# Create your models here.
class SiteUsers(GoogleUser):
	@property
	def sites(self):
		return Sites.gql("WHERE user = :user AND deleted = False", user=self).fetch(1000)

class Sites(db.Model):
	url = db.LinkProperty()
	activate_code = db.StringProperty()
	activated = db.BooleanProperty(default=False)
	user = db.ReferenceProperty(SiteUsers)
	deleted = db.BooleanProperty(default=False)

