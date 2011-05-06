# -*- coding: utf-8 -*-

from kay.utils import forms
from kay.utils.validators import ValidationError
import re


class SettingForm(forms.Form):
	url_re = re.compile("^https?:\/\/[-_.!~*'()a-zA-Z0-9;\/?:\@&=+\$,%#]+$")
	url = forms.TextField("URL", required=True)

	def validate_url(self, value):
		if not self.url_re.match(value):
			raise ValidationError(u'The value must URL format.')
