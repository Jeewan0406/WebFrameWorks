from django.shortcuts import render

def home(request):
    # This looks for 'index.html' inside the templates folder
    return render(request, 'index.html')