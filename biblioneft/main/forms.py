from datetime import date
import re
from django import forms
from .models import User


class LoginForm(forms.Form):
    phone = forms.CharField(label="Телефон", max_length=18, widget=forms.TextInput(attrs={"placeholder": 'Номер телефона'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": 'Введите пароль'}))


class ValidationError(Exception):
    pass


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
            "surname": forms.TextInput(attrs={
                "placeholder": "Введите фамилию",
                "required": True,
                "pattern": "[А-Яа-яЁё]+",
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Введите имя",
                "required": True,
                "pattern": "[А-Яа-яЁё]+",
            }),
            "lastname": forms.TextInput(attrs={
                "placeholder": "Введите отчество",
                "pattern": "[А-Яа-яЁё]+",
            }),
            "date_of_birth": forms.DateInput(attrs={
                "placeholder": "дд.мм.гггг",
                "type": "date",
                "required": True,
                "max": date.today().strftime("%Y-%m-%d"),
            }),
            "education": forms.TextInput(attrs={
                "placeholder": "Введите образование",
                "pattern": "[А-Яа-яЁё]+",
                "required": True,
            }),
            "prof": forms.TextInput(attrs={
                "placeholder": "Введите профессию",
                "pattern": "[А-Яа-яЁё]+",
                "required": True,
            }),
            "study_work": forms.TextInput(attrs={
                "placeholder": "Введите место учебы/работы",
                "pattern": "[А-Яа-яЁё]+",
                "required": True,
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Введите телефон",
                "required": True,
                "pattern": "\+7\d{10}",
                'id': "tel",
            }),
            "passport": forms.TextInput(attrs={
                "placeholder": "Введите паспортные данные",
                "required": True,
                "pattern": "\d{10}",
                'id': "passport",
            }),
            "given": forms.TextInput(attrs={
                "placeholder": "Кем выдан паспорт",
                "pattern": "[А-Яа-яЁё ]+",
                "required": True,
            }),
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth > date.today():
            raise ValidationError("Дата рождения не может быть в будущем.")
        return date_of_birth

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if not re.match(r'^[А-Яа-яЁё]+$', surname):
            raise ValidationError("Фамилия должна содержать только русские буквы.")
        return surname

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[А-Яа-яЁё]+$', name):
            raise ValidationError("Имя должно содержать только русские буквы.")
        return name

    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if lastname and not re.match(r'^[А-Яа-яЁё]+$', lastname):  # Отчество может быть пустым
            raise ValidationError("Имя должно содержать только русские буквы.")
        return lastname
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Пароли не совпадают")
        return cleaned_data
