from django.urls import path, include
from . import views

app_name='sform'

urlpatterns = [
    path('', views.survey, name='survey'),
]
