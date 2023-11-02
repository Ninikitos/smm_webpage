from django.shortcuts import render
from .models import AboutPageModel

# Create your views here.
def index(request):
    return render(request, "webapp/index.html", {})

def about_us(request):
    about_content = AboutPageModel.objects.first()
    return render(request, "webapp/about_us.html", {
        'about_content': about_content
    })


def services(request):
    return render(request, "webapp/services.html", {})


def portfolio(request):
    return render(request, "webapp/portfolio.html", {})


def coaching(request):
    return render(request, "webapp/coaching.html", {})


def contact(request):
    return render(request, "webapp/contact.html", {})
