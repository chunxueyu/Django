from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Book(models.Model):
    name = models.CharField(
        verbose_name="书名",
        max_length=20
    )
    content = HTMLField()