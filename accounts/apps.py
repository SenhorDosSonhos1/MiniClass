from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.db.models.signals import post_save

        from django.contrib.auth import get_user_model
        from accounts.signals import created_user_profile

        