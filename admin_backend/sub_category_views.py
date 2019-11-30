from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from admin_backend.forms.sub_category_form import SubCategoryForm
from admin_backend.models import SubCategory


@login_required
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


@login_required
def sub_category_delete(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk)
    sub_category_data.delete()
    messages.success(request, 'Sub Category Deleted Successfully')
    return HttpResponseRedirect(reverse('sub_category'))


@login_required
def sub_category_status(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk)
    if sub_category_data.sub_category_status:
        sub_category_data.sub_category_status = 0
        messages.warning(request, 'Successfully Status Updated Into Inactive')
    else:
        sub_category_data.sub_category_status = 1
        messages.success(request, 'Successfully Status Updated Into Active')
    sub_category_data.save()
    return HttpResponseRedirect(reverse('sub_category'))


@login_required
def sub_category_edit(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(instance=sub_category_data)
    if request.method == "POST":
        form = SubCategoryForm(request.POST, instance=sub_category_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Sub Category Added Successfully')
            return HttpResponseRedirect(reverse('sub_category'))
    context = {
        'form': form
    }
    return render(request, 'Backend/SubCategory/edit_subcategory.html', context)
