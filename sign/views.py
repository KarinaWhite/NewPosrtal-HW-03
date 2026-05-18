from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework import permissions
from .models import MyModel, Category
from .serializers import MyModelSerializer, CategorySerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Index(View):
    def get(self, request):
        string = _('Hello world')
        return HttpResponse(string)
