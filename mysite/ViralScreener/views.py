from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='ViralScreener/home.html',
                  context = {})