from django.http import HttpResponse
from django.shortcuts import render
from admin_backend.forms.category_form import CategoryForm
from rest_framework.views import APIView
from rest_framework.response import Response
from admin_backend.serializers.category_serializer import CategorySerializer
from .models import Category


def category(request):
    form = CategoryForm()
    context = {
        'title': 'Category',
        'form': form
    }
    return render(request, 'Backend/Category/category.html', context)


class CategoryApi(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            context = {
                'status': 201,
                'data': serializer.data
            }
        else:
            context = {
                'status': 400,
                'errors': serializer.errors,
            }
        return Response(context)
