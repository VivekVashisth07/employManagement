from home.views import Home
from django.urls import path

urlpatterns = [
    path('', Home.as_view()),
    path('addDetails/', Home.add_details),
]
