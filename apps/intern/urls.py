from django.urls import path

from apps.intern import views
from apps.intern.views import Sign, Login, HomeView, logout_view

app_name = "intern"

urlpatterns = [

    path('dashboard/',HomeView.as_view(), name='home'),

]