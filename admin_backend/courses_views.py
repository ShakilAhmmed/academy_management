from django.http import HttpResponse
from django.shortcuts import render

from admin_backend.forms.course_form import CourseForm


def courses(request):
    form = CourseForm()
    context = {
        'form': form
    }
    return render(request, 'Backend/Courses/courses.html', context)
