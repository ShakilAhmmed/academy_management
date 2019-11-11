from django.http import HttpResponse, Http404
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


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a categpry instance.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        deleted=category.delete()
        return Response({'status': 204}) if deleted else Response({'status': 404})
