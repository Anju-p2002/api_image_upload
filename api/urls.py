from django.urls import path
from . import views
from .views import display_api_data
from .views import ImageDataListCreateView, ImageDataDetailView

urlpatterns = [
    path('', display_api_data, name='display_api_data'),
    path('hh/', views.upload_page, name='upload_page'),
    path('images/', ImageDataListCreateView.as_view()),
    path('images/', ImageDataListCreateView.as_view()),
    path('images/<int:pk>/', ImageDataDetailView.as_view()),
]

