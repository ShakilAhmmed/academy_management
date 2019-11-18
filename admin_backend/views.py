from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def admin_home(request):
    context = {
        'title': 'Admin'
    }
    return render(request, 'Backend/admin_home.html', context)
