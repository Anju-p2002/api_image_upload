from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics
from .models import ImageData
from .serializers import ImageDataSerializer
import requests


class ImageDataListCreateView(generics.ListCreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer


class ImageDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer




def delete_image(request, id):

    data = get_object_or_404(ImageData, id=id)

    if data.image:
        data.image.delete()

    data.delete()

    return redirect('/')



def upload_page(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        image = request.FILES.get('image')
        desc = request.POST.get('description')

        ImageData.objects.create(
            name=name,
            image=image,
            description=desc
        )

        return redirect('/')

    return render(request, 'upload.html')

   

# def get_image(request):

#     response = requests.get('http://127.0.0.1:8000/images')

#     if response.status_code == 200:
#         data = response.json()  
#     else:
#         data = {"error": "Could not fetch data"}

#     return render(request, 'display.html', {'data': data})




def get_api_data(request):
    url = "http://127.0.0.1:8000/images"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  
    else:
        data = {"error": "Could not retrieve data"}

    return render(request, 'display.html', {'api_data': data})

# views.py

import requests
from django.shortcuts import render


def display_api_data(request):

    url = 'http://127.0.0.1:8000/images/'

    response = requests.get(url)

    data = response.json()

    return render(request, 'display.html', {'data': data})