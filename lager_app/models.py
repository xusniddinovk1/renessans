from django.db import models


class AboutUs(models.Model):
    context_uz = models.TextField()
    context_ru = models.TextField()
    context_en = models.TextField()

    def __str__(self):
        return self.context_uz[:50]


class Photos(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)


class Activity(models.Model):
    title_uz = models.CharField(max_length=100, null=False, blank=False)
    title_ru = models.CharField(max_length=100, null=False, blank=False)
    title_en = models.CharField(max_length=100, null=False, blank=False)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

    def __str__(self):
        return self.title_uz[:30]


class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    title_uz = models.CharField(max_length=100, null=False, blank=False)
    title_ru = models.CharField(max_length=100, null=False, blank=False)
    title_en = models.CharField(max_length=100, null=False, blank=False)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to='educations/', blank=True, null=True)


class RecreationZone(models.Model):
    title_uz = models.CharField(max_length=100, null=False, blank=False)
    title_ru = models.CharField(max_length=100, null=False, blank=False)
    title_en = models.CharField(max_length=100, null=False, blank=False)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to='recreation/', blank=True, null=True)

    def __str__(self):
        return self.title_uz


class News(models.Model):
    title_uz = models.CharField(max_length=100, null=False, blank=False)
    title_ru = models.CharField(max_length=100, null=False, blank=False)
    title_en = models.CharField(max_length=100, null=False, blank=False)
    content_uz = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz
