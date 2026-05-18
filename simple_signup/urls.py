from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sign.views import NewsViewSet, ArticlesViewSet


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'articles', ArticlesViewSet, basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

    path('api/', include(router.urls)),
]