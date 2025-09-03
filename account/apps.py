from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name',email]