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
from admin.models import *
import urllib2
import logging

# Create your views here.

def _invalid_configuration(request):
	u = request.user
	if not u.sites:
		return True

	return False

def _redirect_configuration(request):
	return redirect(url_for('admin/settings'))

def _activate_code():
	import random
	codes = "asdfghjkqwertyuopzxcvbnm1234567890ASDFGHJKLZXCVBNMQWERTYUOP"
	random_strs = [random.choice(codes) for x in range(36)]
	return ''.join(random_strs)

@login_required
def index(request):
	if _invalid_configuration(request): return _redirect_configuration(request)

	return render_to_response('admin/index.html', {'message': 'Hello'})

@login_required
def settings(request):
	return render_to_response('admin/settings.html')

@login_required
def site_edit(request):
	form = SettingForm()
	if request.method == "POST" and (request.form.has_key('delete') and request.form['delete'] == 'on'):
		if request.form['edit']:
			site = Sites.get(request.form['site'])
			if site.user != request.user: redirect(url_for('admin/settings')) #FIXME error
			site.delete()
		return redirect(url_for('admin/settings'))
	if request.method == "POST" and form.validate(request.form):
		if form.data['edit']:
			site = Sites.get(form.data['site'])
			if site.user != request.user: redirect(url_for('admin/settings')) #FIXME error
		else:
			site = Sites(activate_code=_activate_code(), user=request.user)
			site.url = db.Link(form['url'])
		site.put()
		return redirect(url_for('admin/settings'))
	if request.method == "GET":
		if request.args.has_key('site') and request.args['site']:
			site = Sites.get(request.args['site'])
			if site.user == request.user:
				form.data['url'] = site.url
				form.data['edit'] = '1'
				form.data['site'] = request.args['site']
				form.data['activate_code'] = site.activate_code

	form.delete.widget.value = u'False'
	return render_to_response('admin/site_edit.html', {'form': form.as_widget()})

@login_required
def thermographies(request):
	if _invalid_configuration(request): return _redirect_configuration(request)
	
	site = None
	_thermographies = None
	if request.args.has_key('site'):
		site = Sites.get(request.args['site'])
		if site.user != request.user: return _redirect_configuration(request)
		from thermography.models import ThermographyPointDaily
		_thermographies = ThermographyPointDaily.all().filter('site =',site).order('-date').fetch(1000)

	return render_to_response('admin/thermographies.html', {"site":site, "thermographies":_thermographies})

@login_required
def thermography(request):
	if _invalid_configuration(request): return _redirect_configuration(request)

	if not request.args.has_key('url') or not request.args.has_key('date'):
		#FIXME error
		pass
	
	_thermography = _get_thermography(request.args['url'], request.args['date'])
	logging.info(_thermography)
	if not _thermography or _thermography.site.user != request.user:
		return _redirect_configuration(request)
	
	points_json = _thermography.data
	max_point = _thermography.max_point

	import time
	return render_to_response('admin/thermography.html', {"time":time.time(), "url":_thermography.url, "points":points_json, "max_point":max_point})

@login_required
def site_view(request):
	if _invalid_configuration(request): return _redirect_configuration(request)
	url = request.args['url'] if request.args.has_key('url') else None
	if not url: return redirect(url_for('admin/'))
	
	from xml.sax.saxutils import *
	html = urllib2.urlopen(url).read()
	html = unicode(html, 'utf8', 'ignore')
	return render_to_response('admin/site_view.html', {"html":html})

def _get_site_page(url):
	from thermography.models import ThermographyPointDaily
	_thermographies = ThermographyPointDaily.gql("url =", url.rstrip('/')).fetch(1)
	return _thermographies[0] if _thermographies else None

def _get_thermography(url, date):
	logging.info("%s %s" % (url, date))
	from thermography.models import ThermographyPointDaily
	_thermographies = ThermographyPointDaily.gql("WHERE url=:url AND date=:date", url=url.rstrip('/'), date=date).fetch(1)
	logging.info(_thermographies)
	return _thermographies[0] if _thermographies else None
