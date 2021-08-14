from django.db import models

# Create your models here.
class TemplateModel(models.Model):
    Id = models.IntegerField(primary_key=True)
