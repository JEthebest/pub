from django.contrib import admin
from django.urls import path, include

from drinks import views


drinks_url = [
    path('', views.BeerView.as_view(), name='beer'),
]

urlpatterns = [
    path('mura/pub/', admin.site.urls),
    path('', include(drinks_url)),
]
