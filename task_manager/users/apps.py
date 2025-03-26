import json
import os
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from .signals import load_users_from_json
        post_migrate.connect(load_users_from_json, sender=self)

