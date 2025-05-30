from django.db import models


class AboutUs(models.Model):
    context = models.TextField()

    def __str__(self):
        return self.context[:50]


class Photos(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)


class Activity(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='educations/', blank=True, null=True)


class RecreationZone(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='recreation/', blank=True, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
