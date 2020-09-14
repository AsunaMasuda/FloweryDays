from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address_line_1', 'address_line_2', 'postcode', 'town_or_city', 'county', 'is_gift_wrapping')

    super().__init__(*args, **kwargs)
    placeholders= {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email Address',
        'address_line_1': 'Address Line 1',
        'address_line_2': 'Address Line 2',
        'town_or_city': 'Town or City Name',
        'country': 'County',
        'postcode': 'Postcode',
        'is_gift_wrapping': 'Gift Wrapping',
    }

    self.fields['first_name'].widget.attrs['autofocus'] = True
    # the curser will start in the first name field when the page is loaded.

    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
            # Adding * to the placeholder's required field
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs.['placeholder'] = placeholder
        self.fields[field].widget.attrs.['class'] = 'stripe-style-input'
        self.fields[field].label = False # removing the form fields labels