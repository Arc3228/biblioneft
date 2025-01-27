from django import forms
from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(label="Телефон", max_length=20)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "name",
            "surname",
            "lastname",
            "date_of_birth",
            "education",
            "prof",
            "study_work",
            "phone",
            "passport",
            "given",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data