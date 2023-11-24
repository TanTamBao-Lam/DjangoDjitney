from typing import Any
from django.shortcuts import render

from .models import Line, Stop, Station
from .forms import StopForm, LineForm, StationForm

# Import views templates
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

"""
Views for Lines: list view, CRUD views.
"""
# List View of Lines
class LinesView(ListView):
    model = Line
    template_name = "routes/lines.html"
    
# Create Lines view
class CreateLineView(CreateView):
    model = Line
    template_name = "routes/add_line.html"
    form_class = LineForm
    
# Update Lines View
class UpdateLineView(UpdateView):
    model = Line
    template_name = "routes/update_line.html"
    form_class = LineForm
    
# Delete Lines View
class DeleteLineView(DeleteView):
    model = Line
    template_name = "routes/delete_line.html"
    # Need to define a success_url after delete is success.
    success_url = reverse_lazy("lines")
    

"""
Views for Station
"""
class StationsView(ListView):
    model = Station
    template_name = "routes/stations.html"
    

class CreateStationView(CreateView):
    model = Station
    template_name = "routes/add_station.html"
    form_class = StationForm
    
class UpdateStationView(UpdateView):
    model = Station
    template_name = "routes/update_station.html"
    form_class = StationForm
    
class DeleteStationView(DeleteView):
    model = Station
    template_name = "routes/delete_station.html"
    success_url = reverse_lazy("stations")
    
    
"""
Views for Stops
"""
class StopView(ListView):
    model = Stop
    template_name = "routes/stops.html"
    
class CreateStopView(CreateView):
    model = Stop
    template_name = "routes/add_stop.html"
    form_class = StopForm
    
class UpdateStopView(UpdateView):
    model = Stop
    template_name = "routes/update_stop.html"
    form_class = StopForm
    
class DeleteStopView(DeleteView):
    model = Stop
    template_name = "routes/delete_stop.html"
    success_url = reverse_lazy("stops")