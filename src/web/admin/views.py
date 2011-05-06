# -*- coding: utf-8 -*-
"""
admin.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from kay.utils import render_to_response
from kay.utils import url_for
from kay.auth.decorators import login_required
from werkzeug import redirect
from admin.forms import SettingForm
import logging

# Create your views here.

def _invalid_configuration(request):
	u = request.user
	if not u.activate_code:
		u.activate_code = _activate_code()
		u.put()

	if u.url is None:
		return True

	return False

def _redirect_configuration(request):
	return redirect(url_for('admin/settings'))

def _activate_code():
	import random
	codes = "asdfghjklqwertyuiopzxcvbnm1234567890ASDFGHJKLZXCVBNMQWERTYUIOP"
	random_strs = [random.choice(codes) for x in range(36)]
	return ''.join(random_strs)

@login_required
def index(request):
	if _invalid_configuration(request): return _redirect_configuration(request)

	return render_to_response('admin/index.html', {'message': 'Hello'})

@login_required
def settings(request):
	u = request.user
	form = SettingForm()
	if request.method == "POST" and form.validate(request.form):
		u.url = form.data['url']
		u.put()
	elif request.method == "GET":
		form.data['url'] = u.url

	return render_to_response('admin/settings.html', {'form': form.as_widget()})

@login_required
def thermography(request):
	if _invalid_configuration(request): return _redirect_configuration(request)
	
	return render_to_response('admin/thermography.html', {})
