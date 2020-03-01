from django.db import models


class Disorders(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField('Symptom',  blank=True)


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return (self.name + " " + self.frequency)


class Symptoms(models.Model):
    name = models.CharField(max_length=100)
    disorders = models.ManyToManyField('Disorder', blank=False)

    def __str__(self):
        return (self.name)


class Disorder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
