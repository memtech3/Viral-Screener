from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='ViralScreener/home.html',
                  context = {})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("ViralScreener:homepage")