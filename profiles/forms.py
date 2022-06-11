from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    User Profile in My Account
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Calls original init method to set up form as default
        and then renders it with set placeholder classes and auto-focus
        on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address',
            'default_optional_address': 'Optional Street Address',
            'default_postcode': 'Postal Code',
            'default_city': 'City',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:

                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = (
                    'border-black rounded-0'
                )
                self.fields[field].label = False
                self.fields['default_country'].label = False
