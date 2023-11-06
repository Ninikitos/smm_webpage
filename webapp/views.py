from django.shortcuts import render
from .models import AboutPageModel, ServicePageModel, CoachingPageModel

# Create your views here.
def index(request):
    return render(request, "webapp/index.html", {})

def about_us(request):
    about_content = AboutPageModel.objects.first()
    return render(request, "webapp/about_us.html", {
        'about_content': about_content
    })


def services(request):
    service_content = ServicePageModel.objects.first()
    return render(request, "webapp/services.html", {
        'service_content': service_content
    })


def portfolio(request):
    return render(request, "webapp/portfolio.html", {})


def coaching(request):
    coaching_content = CoachingPageModel.objects.first()
    return render(request, "webapp/coaching.html", {
        'coaching_content': coaching_content
    })


def contact(request):
    return render(request, "webapp/contact.html", {})
