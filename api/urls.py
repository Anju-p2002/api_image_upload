from django.urls import path
from . import views
from .views import ImageDataListCreateView, ImageDataDetailView

urlpatterns = [
    path('', views.upload_page, name='upload_page'),
    path('images/', ImageDataListCreateView.as_view()),
    path('images/<int:pk>/', ImageDataDetailView.as_view()),
]

