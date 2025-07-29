from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_viewer_page, name='file_viewer_page'),
]