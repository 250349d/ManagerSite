from django.apps import AppConfig


class LoginAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_app'

    def ready(self):
        from login_app.utils import signals
