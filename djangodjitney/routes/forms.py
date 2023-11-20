from django import forms
from .models import Stop, Station, Line

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = "__all__"
        
        
class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = "__all__"
        

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = "__all__"
