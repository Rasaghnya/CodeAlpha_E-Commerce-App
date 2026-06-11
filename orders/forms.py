from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }
        )
    )

    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }
        )
    )

    shipping_address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Shipping address'
            }
        )
    )

    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }
        )
    )

    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'State'
            }
        )
    )

    zipcode = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Zipcode'
            }
        )
    )

    payment_method = forms.ChoiceField(
        choices=[
            ('COD', 'Cash On Delivery'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )
