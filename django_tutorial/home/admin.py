from django.contrib import admin

# Register your models here.
from .models import Departments,Doctors,Booking

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','book_date',
                    'booked_on','amount','order_id','razorpay_id','pay_status')


admin.site.register(Booking,BookingAdmin)
