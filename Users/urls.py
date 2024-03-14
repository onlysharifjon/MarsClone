from django.urls import path
from .views import AllStudents,BittaOquvchi
urlpatterns = [
    path('hammaoquvchi/',AllStudents.as_view()),
    path('bitta/',BittaOquvchi.as_view())
]