# -*- coding: utf-8 -*-
# admin.models

from google.appengine.ext import db
from kay.auth.models import GoogleUser

# Create your models here.
class SiteUsers(GoogleUser):
	url = db.TextProperty()
	activate_code = db.StringProperty()
