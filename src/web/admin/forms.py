# -*- coding: utf-8 -*-

from kay.utils import forms
from kay.utils.validators import ValidationError
from admin.models import *
import re


class SettingForm(forms.Form):
	url_re = re.compile("^https?:\/\/[-_.!~*'()a-zA-Z0-9;\/?:\@&=+\$,%#]+$")
	url = forms.TextField("URL", required=True)
	activate_code = forms.TextField("Activate Code")
	edit = forms.TextField("Edit Mode", widget=forms.HiddenInput)
	site = forms.TextField("Site Key", widget=forms.HiddenInput)
	delete = forms.Field("Delete", widget=forms.Checkbox, default='1')

	def validate_url(self, value):
		if not self.url_re.match(value):
			raise ValidationError(u'The value must URL format.')

		cur_site = None
		if self.raw_data['edit']:
			cur_site = Sites.get(self.raw_data['site'])
			if cur_site.user != self.request.user:
				raise ValidationError(u'Invalid arguments.')

		for site in self.request.user.sites:
			if (cur_site is not None and cur_site.key() != site.key()) and value.startswith(site.url.rstrip('/')):
				raise ValidationError(u'The URL is already exists.')
