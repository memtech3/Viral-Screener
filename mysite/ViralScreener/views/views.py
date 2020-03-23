from .imports import *
#Put all views that don't belong elsewere here
@login_required
def homepage(request):
    return render(request, 'ViralScreener/home.html',
    context = {"AlertMessage":AlertMessage.objects.all})

