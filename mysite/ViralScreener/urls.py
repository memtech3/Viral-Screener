from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'ViralScreener'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    url("screening/", views.screening, name="screening"),
    url('login/', views.login_request, name='login'),
    url("logout/", views.logout_request, name="logout"),
]