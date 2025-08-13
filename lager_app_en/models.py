from django.db import models


class AboutUs1(models.Model):
    context = models.TextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.context[:50]


class Photos1(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)


class Activity1(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

    def __str__(self):
        return self.title


class Hotel1(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education1(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='educations/', blank=True, null=True)


class RecreationZone1(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='recreation/', blank=True, null=True)

    def __str__(self):
        return self.title


class News1(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
