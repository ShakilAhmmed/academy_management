from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from admin_backend.forms.sub_category_form import SubCategoryForm
from admin_backend.models import SubCategory


def sub_category(request):
    sub_category = SubCategory.objects.select_related().all()
    if request.method == "POST":
        form = SubCategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Sub Category Added Successfully')
            return HttpResponseRedirect(reverse('sub_category'))

    else:
        form = SubCategoryForm()
    context = {
        'form': form,
        'title': 'Sub Category',
        'sub_category': sub_category
    }
    return render(request, 'Backend/SubCategory/sub_category.html', context)
