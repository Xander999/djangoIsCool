from django.db import models

class Student(models.Model):
    #id = models.AutoField()   <- this is auto field
    name  = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()


class Car(models.Model):
    carName = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.carName+' '+str(self.speed)
