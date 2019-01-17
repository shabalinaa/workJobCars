from django.db import models
from django.utils import timezone


'''class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title'''

class Car(models.Model):
    color = models.CharField(max_length=30)
    number = models.IntegerField()
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.model

class Driver(models.Model):
    fio = models.CharField(max_length=30)
    experience = models.IntegerField()

    def __str__(self):
        return self.fio

class Crew(models.Model):
    name = models.CharField(max_length=30)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name