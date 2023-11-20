from typing import Any
from django.shortcuts import render

from .models import Line, Stop, Station
from .forms import StopForm, LineForm, StationForm

from django.views.generic import TemplateView

# Create your views here.
# home views
class HomeView(TemplateView):
    template_name = "routes/home.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context["lines"] = Line.objects.all()
        context["stations"] = Station.objects.all()
        context["stops"] = Stop.objects.all()
        
        return context
