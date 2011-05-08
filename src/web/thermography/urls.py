# -*- coding: utf-8 -*-
# thermography.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('thermography/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'thermography/index': 'thermography.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='thermography.views.index'),
    Rule('/track', endpoint='track', view='thermography.views.track'),
    Rule('/task_calculate_points', endpoint='task_calculate_points', view='thermography.views.task_calculate_points'),
    Rule('/task_calculate_point_daily', endpoint='task_calculate_point_daily', view='thermography.views.task_calculate_point_daily'),
    Rule('/task_calculate_point_month', endpoint='task_calculate_point_month', view='thermography.views.task_calculate_point_month'),
  )
]

