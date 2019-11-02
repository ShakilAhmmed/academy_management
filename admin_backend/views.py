from django.shortcuts import render


# Create your views here.
def admin_home(request):
    context = {
        'title': 'Admin'
    }
    return render(request, 'Backend/admin_home.html', context)
