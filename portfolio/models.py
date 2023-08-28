from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length = 1000)
    image = ImageField(upload_to='portfolio/images/')
    repository_url = URLField(blank=True)
    deploy_url = URLField(blank=True)

    def __str__(self) -> str:
        return self.title