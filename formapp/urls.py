from django.urls import path, include
from .views import QuestionareAll



urlpatterns = [
    path('forms/unclaimed', QuestionareAll.as_view(), name='unclaimed_leads'),
]