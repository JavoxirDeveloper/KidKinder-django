from django.db import models

# Create your models here.
class Classes(models.Model):
    foto = models.ImageField(upload_to="media/classes", blank=False)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
# Informations --->
    kids_age = models.IntegerField(blank=False)
    total_seats = models.IntegerField(blank=False)
    class_time = models.TimeField(auto_now=False, auto_now_add=False)
    course_price = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

class Teachers(models.Model):
    img = models.ImageField(upload_to="media/Teachers", blank=False)
    ful_name = models.CharField(max_length=100, blank=False)
    specialty = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.ful_name

class Gallery(models.Model):
    image = models.ImageField(upload_to="media/Gallery", blank=False)
    image_comment = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.image_comment

class Massage(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    select_class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class ContactMassage(models.Model):
    your_name = models.CharField(max_length=200, blank=False)
    your_email = models.EmailField(blank=False)
    subject = models.CharField(max_length=200, blank=False)
    massage = models.TextField(blank=True)