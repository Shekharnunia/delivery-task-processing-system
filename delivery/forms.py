from django import forms

from .models import DeliveryTask


class DeliveryTaskForm(forms.ModelForm):

    class Meta:
        model = DeliveryTask
        fields = ['title', 'priority', ]
