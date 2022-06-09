from django import forms


class ContactForm(forms.Form):
    """
    Contact form for business
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    company = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'