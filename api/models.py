# from django.db import models

# class ImageData(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='images/')
#     def __str__(self):
#         return self.name


from django.db import models

class ImageData(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='images/', null=True, blank=True)

    description = models.TextField()