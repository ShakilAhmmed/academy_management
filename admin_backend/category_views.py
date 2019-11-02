from django.shortcuts import render


def category(request):
    context = {
        'title': 'Category'
    }
    return render(request, 'Backend/Category/category.html', context)
