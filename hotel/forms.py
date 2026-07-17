from django import forms

from .models import Booking, Hotel, Review


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ('title', 'image', 'text', 'price', 'amount', 'capacity')


class HotelSearchForm(forms.Form):
    check_in = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField(required=False, min_value=1)
    min_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guest_name', 'email', 'phone', 'check_in', 'check_out', 'guests', 'comment')
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, hotel=None, **kwargs):
        self.hotel = hotel
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        guests = cleaned_data.get('guests')

        if check_in and check_out:
            if check_in >= check_out:
                raise forms.ValidationError("Check-out date must be after check-in date.")

        if self.hotel and guests and guests > self.hotel.capacity:
            self.add_error('guests', f"This room can accommodate up to {self.hotel.capacity} guests.")

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'text')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'rows': 3}),
        }
