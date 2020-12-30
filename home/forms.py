from django import forms


class ContactForm(forms.Form):
    """
    Contact Form on Landing Page
    """
    SUBJECT_CHOICES = (
        ('Corporate & Event Flower Inquiry',
         'Corporate & Event Flower Inquiry'),
        ('Wedding Flower Inquiry', 'Wedding Flower Inquiry'),
        ('Custom Bouquet Inquiry', 'Custom Bouquet Inquiry'),
        ('Other', 'Other'),
    )

    name = forms.CharField(
        label="Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    subject = forms.CharField(
        label="Subject",
        max_length=3,
        widget=forms.Select(choices=SUBJECT_CHOICES),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 7,
        })
    )

    class Meta:
        fields = ['name', 'email', 'subject', 'message']
