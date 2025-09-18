from django.shortcuts import render

# Create your views here.
"""Homepage"""
def index(request):
    return render(request, 'puddle_app/index.html')

def contact(request):
    return render(request, 'puddle_app/contact.html')
