from django.urls import path
from . import views

urlpatterns = [
    path('api/1/chat/', views.ChatterBotApiView.as_view(), name='chatterbot'),
]
