from .models import Contact
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        """
        Calls original init method to set up form as default
        and then renders it with set placeholder classes and auto-focus
        on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
