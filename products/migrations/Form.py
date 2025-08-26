from django import forms
from .models import feedback

class feedbackForm(forms.modelForm):
    class Meta:
        model = feedback
        fields = ['comment']