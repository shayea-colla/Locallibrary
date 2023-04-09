from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class RenewBookForm(forms.Form):
    
    renewal_date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text="أدخل بياناتك هنا")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']


        # check if data is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if data is not after four weeks from now
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more then 4 weeks'))

        return data
