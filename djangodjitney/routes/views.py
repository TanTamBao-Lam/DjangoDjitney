from django.shortcuts import render


# Create your views here.
# home views
def home(request):
    context_collections = {
        "Title": "Welcome to Django Djitter"
    }
    return render(request, template_name="routes/home.html", context=context_collections)