from django import forms
from django.core.validators import URLValidator

validate = URLValidator()

class UrlTinifyForm(forms.Form):
    url = forms.CharField(max_length=255)

    def clean_url(self):
        url = self.cleaned_data['url']
        validate(url)
        return url