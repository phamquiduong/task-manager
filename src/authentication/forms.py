from django import forms
from django.contrib.auth.password_validation import (CommonPasswordValidator, MinimumLengthValidator,
                                                     NumericPasswordValidator, UserAttributeSimilarityValidator)
from django.core.exceptions import ValidationError

from authentication import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = models.User
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")

        if password:
            validators = [
                CommonPasswordValidator(),
                MinimumLengthValidator(),
                NumericPasswordValidator(),
                UserAttributeSimilarityValidator(),
            ]

            for validator in validators:
                try:
                    validator.validate(password, user=self.instance)
                except ValidationError as error:
                    self.add_error('password', error)

        return cleaned_data
