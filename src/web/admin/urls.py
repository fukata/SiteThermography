# -*- coding: utf-8 -*-
# admin.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('admin/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'admin/index': 'admin.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='admin.views.index'),
    Rule('/settings', endpoint='settings', view='admin.views.settings'),
    Rule('/site_edit', endpoint='site_edit', view='admin.views.site_edit'),
    Rule('/thermographies', endpoint='thermographies', view='admin.views.thermographies'),
    Rule('/thermography', endpoint='thermography', view='admin.views.thermography'),
    Rule('/site_view', endpoint='site_view', view='admin.views.site_view'),
  )
]

