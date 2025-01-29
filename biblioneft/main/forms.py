from django import forms
from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(label="Телефон", max_length=18, widget=forms.TextInput(attrs={"placeholder": 'Номер телефона'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": 'Введите пароль'}))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))
    password_confirm = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите пароль"})
    )

    class Meta:
        model = User
        fields = [
            "surname",
            "name",
            "lastname",
            "date_of_birth",
            "education",
            "prof",
            "study_work",
            "phone",
            "passport",
            "given",
        ]
        labels = {
            "surname": "Фамилия",
            "name": "Имя",
            "lastname": "Отчество",
            "date_of_birth": "Дата рождения",
            "education": "Образование",
            "prof": "Профессия",
            "study_work": "Место учебы/работы",
            "phone": "Телефон",
            "passport": "Паспорт",
            "given": "Кем выдан",
        }
        widgets = {
            "surname": forms.TextInput(attrs={"placeholder": "Введите фамилию"}),
            "name": forms.TextInput(attrs={"placeholder": "Введите имя"}),
            "lastname": forms.TextInput(attrs={"placeholder": "Введите отчество"}),
            "date_of_birth": forms.DateInput(attrs={"placeholder": "Дата рождения", "type": "date"}),
            "education": forms.TextInput(attrs={"placeholder": "Введите образование"}),
            "prof": forms.TextInput(attrs={"placeholder": "Введите профессию"}),
            "study_work": forms.TextInput(attrs={"placeholder": "Введите место учебы/работы"}),
            "phone": forms.TextInput(attrs={"placeholder": "Введите телефон", "id": 'id_phone'}),
            "passport": forms.TextInput(attrs={"placeholder": "Введите паспортные данные", "id": 'id_passport'}),
            "given": forms.TextInput(attrs={"placeholder": "Кем выдан паспорт"}),
            "password": forms.TextInput(attrs={"placeholder": "Пароль", "class": 'password_wrapper'}),
            "password_confirm": forms.TextInput(attrs={"placeholder": "Пароль", "class": 'password_wrapper'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data