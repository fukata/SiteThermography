# -*- coding: utf-8 -*-
"""
thermography.views
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
from kay.utils import render_json_response
from models import *
import json
from datetime import datetime
import logging

# Create your views here.

def index(request):
	return render_to_response('thermography/index.html', {'message': 'Hello'})

def track(request):
	if request.method != "POST":
		return render_json_response({'error':'Invalid method'})
	
	data = json.loads(request.form['data'])
	if len(data['move_events'])==0: 
		return render_json_response({'error':'Invalid arguments'})
	
	t = Thermographies(data=request.form['data'], calculate_status=0)
	t.put()
	return render_json_response({'message':'Tracking successful'})

def task_calculate_points(request):
	thermographies = Thermographies.all().filter("calculate_status =", 0).fetch(1)
	if not thermographies: return render_json_response({'message':'Calculate points unsuccessful'})

	for thermography in thermographies:
		data = json.loads(thermography.data)
		points = {}
		for event in data['move_events']:
			x = int(event['pageX']) / 20
			y = int(event['pageY']) / 20
			key = "%s:%s" % (x, y)
			if points.has_key(key):
				points[key] += 1
			else:
				points[key] = 1

		ts = int(str(data['move_events'][-1]['timeStamp'])[0:10])
		event_time = datetime.fromtimestamp(ts)
		ThermographyPoints(
			thermography = thermography, 
			data = json.dumps(points), 
			year_calculate_status = 0,
			month_calculate_status = 0,
			day_calculate_status = 0,
			date = "%04d%02d%02d" % (event_time.year, event_time.month, event_time.day),
			year = event_time.year,
			month = event_time.month,
			day = event_time.day,
		).put()

		thermography.calculate_status = 1
		thermography.put()

	return render_json_response({'message':'Calculate points successful'})

def task_calculate_point_daily(request):
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	date = "%04d%02d%02d" % (year, month, day)

	thermographies = ThermographyPointDaily.all().filter("date =",date).fetch(1)
	total_points = {}
	if thermographies:
		thermography = thermographies[0]
		total_points = json.loads(thermography.data)
	else:
		thermography = ThermographyPointDaily()
		thermography.date = date
		thermography.year = year
		thermography.month = month
		thermography.day = day
		thermography.maxPoint = 0

	thermography_points = ThermographyPoints.all().filter("day_calculate_status =",0).filter("date =",date).fetch(10)
	logging.info(thermography_points)
	for thermography_point in thermography_points:
		points = json.loads(thermography_point.data)
		for key in points.keys():
			if total_points.has_key(key):
				total_points[key] += points[key]
			else:
				total_points[key] = points[key]

		thermography.data = json.dumps(total_points)
		thermography.maxPoint = max(total_points.values())
		thermography.put()

		thermography_point.day_calculate_status = 1
		thermography_point.put()

	return render_json_response({'message':'Calculate point %s daily successful' % date})
