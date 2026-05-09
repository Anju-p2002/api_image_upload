from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics
from .models import ImageData
from .serializers import ImageDataSerializer


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
        desc = request.POST.get('image_description')

        ImageData.objects.create(
            name=name,
            image=image,
            description=desc
        )

        return redirect('/')

    return render(request, 'upload.html')

    