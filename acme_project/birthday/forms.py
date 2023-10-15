from django import forms

from .models import Birthady


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthady
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
