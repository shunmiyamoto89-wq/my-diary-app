# pages/urls.py
from django.urls import path
# ↓ MonthArchiveView を追加しました
from .views import HomePageView, DiaryDetailView, MonthArchiveView 
from django.views.generic import TemplateView
from .views import ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('diary/<int:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('archive/<int:year>/<int:month>/', MonthArchiveView.as_view(), name='month_archive'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]