from datetime import date
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from ckeditor.fields import RichTextField # type: ignore


class Course(models.Model):
    course_name = models.CharField(max_length=45)
    price = models.FloatField()

    def __str__(self):
        return self.course_name
    
class Module(models.Model):
    module_name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.module_name

class Lesson(models.Model):
    title = models.CharField(max_length=55)
    content = RichTextField(blank=True, null=True)
    module = models.ForeignKey(Module, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Ressource(models.Model):
    links = models.CharField(max_length=255)
    image = models.ImageField()
    video_file = models.FileField(default=True)
    lesson = models.ForeignKey(Lesson,null=True, on_delete=models.CASCADE)




class Stripe(models.Model):
    name_product = models.CharField(max_length=55)
    client = models.ForeignKey(User,  on_delete=models.CASCADE)
    name_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price_product = models.FloatField()
    number_card = models.CharField(max_length=255, default="card")
    expiry = models.DateField(default=date.today)
    cvc = models.CharField(max_length=255, default="cvc")
    country = models.CharField(max_length=255, default="country")
    zip_code = models.CharField(max_length=255, default="0000")

