from django.urls import path
from . import views


app_name = 'ViralScreener'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("logout", views.logout_request, name="logout"),
]