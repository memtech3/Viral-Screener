from .imports import *
#Put all views that don't belong elsewere here
@login_required
def homepage(request):
    return render(request, 'ViralScreener/home.html',
    context = {"AlertMessage":AlertMessage.objects.all})

@login_required
def screening(request):
    return render(request, 'ViralScreener/screening.html',
    context = {"AlertMessage":AlertMessage.objects.all})
