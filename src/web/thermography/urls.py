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
  )
]

