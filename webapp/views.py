from django.shortcuts import render
from django.template.loader import render_to_string

from .models import AboutPageModel, ServicePageModel, CoachingPageModel, ClientInformation
from django.http import HttpResponseRedirect

from django.core.mail import EmailMessage
from django.conf import settings

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
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company', '')
        scope = request.POST.get('scope', '')
        work = request.POST.get('work', '')
        social = request.POST.get('social', '')
        services = ', '.join(request.POST.getlist('service', []))
        is_social_agency = request.POST.get('is_social_agency', '')
        is_social_agency = 'Yes' if is_social_agency == 'yes' else 'No'
        budget = request.POST.get('budget', None)
        start_date = request.POST.get('start-date', None)
        message = request.POST.get('message', '')

        # Create an instance of the model and save the data
        ClientInformation.objects.create(
            name=name,
            lastname=lastname,
            email=email,
            phone=phone,
            company=company,
            scope=scope,
            work=work,
            social=social,
            services=services,
            is_social_agency=is_social_agency,
            budget=budget,
            start_date=start_date,
            message=message
        )
        # Email to predefined address with all data information
        message = f"New client: {name} {lastname} completed a form."
        email = EmailMessage(
            'New client request from a website',
                message,
            settings.EMAIL_HOST_USER,
            ['ninikitos90@gmail.com' ,'alina.banit11@gmail.com']
        )
        email.send()
        return HttpResponseRedirect("thank_you")
    else:
        return render(request, "webapp/contact.html")


def thank_you(request):
    return render(request, 'webapp/thank_you.html')