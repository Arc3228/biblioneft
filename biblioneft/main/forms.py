from django import forms
from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(label="Телефон", max_length=18)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "Фамилия",
            "Имя",
            "Отчество",
            "Дата рождения",
            "Образование",
            "Профессия",
            "Место учёбы/работы",
            "Контактный телефон",
            "Паспортные данные",
            "Кем выдан",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data