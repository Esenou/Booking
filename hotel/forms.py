from django import forms

from .models import Booking, Hotel


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ('title', 'image', 'text', 'price', 'amount')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guest_name', 'email', 'phone', 'check_in', 'check_out', 'guests', 'comment')
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out:
            if check_in >= check_out:
                raise forms.ValidationError("Check-out date must be after check-in date.")

        return cleaned_data
