from django import forms
from ticketprocess.models import bus
class busform(forms.ModelForm):
    class Meta:
        model = bus
        fields= '__all__'
