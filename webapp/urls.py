from django.urls import path
from . import views
from .views import PortfolioJsonView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about-us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/portfolio-json/<int:num_projects>/', PortfolioJsonView.as_view(), name='portfolio-json'),
    path('coaching/', views.coaching, name='coaching'),
    path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank-you'),
    path('portfolio/<slug:slug>', views.project_detail, name='project-detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
