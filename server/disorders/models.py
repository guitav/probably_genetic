from django.db import models


class Disorder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    disorders = models.ManyToManyField('Disorder', related_name="symptom_list", blank=False)

    def __str__(self):
        return self.name
