import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from lager_app.models import (
    Photos, Activity, Hotel, Education,
    RecreationZone, News
)


# 📌 Foydalanuvchi rasm o‘chirganda — faylni ham o‘chirish
@receiver(post_delete, sender=Photos)
@receiver(post_delete, sender=Activity)
@receiver(post_delete, sender=Hotel)
@receiver(post_delete, sender=Education)
@receiver(post_delete, sender=RecreationZone)
@receiver(post_delete, sender=News)
def delete_image_on_delete(sender, instance, **kwargs):
    image_field = getattr(instance, 'image', None)
    if image_field and image_field.name and default_storage.exists(image_field.name):
        default_storage.delete(image_field.name)


# 📌 Foydalanuvchi rasmni yangilaganda — eski faylni o‘chirish
@receiver(pre_save, sender=Photos)
@receiver(pre_save, sender=Activity)
@receiver(pre_save, sender=Hotel)
@receiver(pre_save, sender=Education)
@receiver(pre_save, sender=RecreationZone)
@receiver(pre_save, sender=News)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # yangi obyekt

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    old_file = getattr(old_instance, 'image', None)
    new_file = getattr(instance, 'image', None)

    if old_file and old_file != new_file:
        if old_file.name and default_storage.exists(old_file.name):
            default_storage.delete(old_file.name)
