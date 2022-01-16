from django.urls import path, include
from .views import QuestionareAll, AssignAgentView



urlpatterns = [
    path('forms/unclaimed', QuestionareAll.as_view(), name='unclaimed_leads'),
    path('forms/<int:id>/claim', AssignAgentView.as_view(), name='claim_lead')
]