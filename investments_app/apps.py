from django.apps import AppConfig


class InvestmentsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investments_app'

    def ready(self):
        import investments_app.signals
