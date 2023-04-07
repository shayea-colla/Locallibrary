from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and four weeks (default three)")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']


        # check if data is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if data is not after four weeks from now
        if data > datatime.date.today() + datetime.timedelta(week=4):
            raise VAlidationError(_('Invalid date - renewal more then 4 weeks'))

        return data
