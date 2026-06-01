from django import forms


class CheckoutForm(forms.Form):

    full_name = forms.CharField(
        max_length=200
    )

    phone_number = forms.CharField(
        max_length=15
    )

    shipping_address = forms.CharField(
        widget=forms.Textarea
    )

    city = forms.CharField(
        max_length=100
    )

    state = forms.CharField(
        max_length=100
    )

    zipcode = forms.CharField(
        max_length=10
    )

    payment_method = forms.ChoiceField(
        choices=[
            ('COD', 'Cash On Delivery'),
        ]
    )