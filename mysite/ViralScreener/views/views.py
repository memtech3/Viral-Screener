from .imports import *
#Put all views that don't belong elsewere here
@login_required
def homepage(request):
    return render(request, 'ViralScreener/home.html',
    context = {"AlertMessage":AlertMessage.objects.all})

@login_required
def employeeScreening(request):
    return render(request, 'ViralScreener/employeeScreening.html',
    context = {"AlertMessage":AlertMessage.objects.all})
