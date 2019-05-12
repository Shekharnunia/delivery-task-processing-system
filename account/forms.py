from django import forms

from .models import User

STATUS = [
    ('is_delivery_person', 'delivery'),
    ('is_store_manager', 'manager'),
]


class SignupForm(forms.Form):
    status = forms.CharField(label='What is your status?', widget=forms.Select(choices=STATUS))

    def signup(self, request, user):
        if self.cleaned_data['status'] == 'is_delivery_person':
            user.is_delivery_person = True
        if self.cleaned_data['status'] == 'is_store_manager':
            user.is_store_manager = True
        user.save()


class UserUpdateForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'required': True}),
    )

    class Meta:
        model = User
        fields = ['name', 'email', ]
