from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'
    label = 'myauth'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)
