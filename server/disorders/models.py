from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    disorders = models.ManyToManyField('Disorder', blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Disorder(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)
