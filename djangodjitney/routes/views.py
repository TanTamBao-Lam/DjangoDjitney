from typing import Any
from django.shortcuts import render

from .models import Line, Stop, Station
from .forms import StopForm, LineForm, StationForm

# Import views templates
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    #__all__ is used to substitute to all fields in the models.
    fields = "__all__"
    
# Update Lines View
class UpdateLineView(UpdateView):
    model = Line
    template_name = "routes/update_line.html"
    fields = "__all__"
    
# Delete Lines View
class DeleteLineView(DeleteView):
    model = Line
    template_name = "routes/delete_line.html"