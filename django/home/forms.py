from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'book_date': DateInput(),
        }

        labels = {
            'p_name' : "Patient Name :",
            'p_phone' : "Patient Phone :",
            'p_email' : "Patient Email :",
            'doc_name' : "Doctor Name :",
            'book_date' : "Booking Date :",
        }