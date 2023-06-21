from django.urls import path

from main import views

urlpatterns = [
    path('newsletter/', views.NewsletterView.as_view({'get': 'list', 'post': 'create'}))
]
