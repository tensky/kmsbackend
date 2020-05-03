from django.db import models


class KmsModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)


class KmsDelete(models.Model):
    document_id = models.CharField(max_length=100)


class KmsUpdate(models.Model):
    document_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)