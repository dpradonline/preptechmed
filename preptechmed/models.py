from django.db import models
from tinymce.models import HTMLField


class Introduction(models.Model):
    intro = HTMLField(blank=True, null=True)

    def __str__(self):
        return 'Introduction'


class Overview(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    overview = HTMLField(blank=True, null=True)

    def __str__(self):
        return 'Overview'


class Point(models.Model):
    question = models.TextField()
    answer = HTMLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    order = models.DecimalField(max_digits=5, decimal_places=2, default='999')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class About(models.Model):
    content = HTMLField(blank=True, null=True)

    def __str__(self):
        return 'About'


class Scripture(models.Model):
    verse = HTMLField(blank=True, null=True)
    reference = models.CharField(max_length=180, blank=True, null=True)

    def __str__(self):
        return self.reference


class FileUpload(models.Model):
    name = models.CharField(max_length=180)
    file = models.FileField()

    def __str__(self):
        return self.name
