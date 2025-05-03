from django.apps import AppConfig


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lager_app'

    def ready(self):
        import lager_app.signals
