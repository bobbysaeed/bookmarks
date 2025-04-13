from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']


    def clean_password2(self):
        """
        Validates that the two password fields match.

        This method is automatically called during form validation to ensure
        that the `password` and `password2` fields contain the same value.
        If the passwords do not match, a ValidationError is raised.

        Returns:
            str: The validated value of the `password2` field.

        Raises:
            forms.ValidationError: If the `password` and `password2` fields do not match.
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    A form for editing user information.

    This form allows users to update their first name, last name, and email address.
    It is based on the user model returned by `get_user_model()`.

    Attributes:
        Meta (class): Specifies the model and fields to include in the form.
            - model: The user model (retrieved using `get_user_model()`).
            - fields: A list of fields to include in the form (`first_name`, `last_name`, `email`).
    """
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


