from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Booking
from .forms import BookingForm
import razorpay

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')





def booking(request):

    if request.method == "POST":

        name = request.POST.get('p_name')
        email = request.POST.get('p_email')

        doc_num = request.POST.get('doc_name')
        doctor_obj = Doctors.objects.get(id=doc_num)
        doc = "Dr. "+doctor_obj.doc_name

        client = razorpay.Client(auth=("rzp_test_BJzMHCR6f7fAac","QZzBZWbmbNnihxu5XM17tyA1"))
        response_pay = client.order.create(dict(amount=50000,currency='INR'))
        
        order_id = response_pay['id']
        order_status = response_pay['status']

        if order_status=='created':
            form = BookingForm(request.POST)
            
            latest_entry = Booking.objects.order_by('-id').first()
            if latest_entry:
                if not latest_entry.order_id:
                    latest_entry.order_id = order_id
                    latest_entry.save()
            
            response_pay['name']=name
            response_pay['email']=email
            response_pay['doctor']=doc

            if form.is_valid():
                form.save()
                return render(request,'payment.html',{'payment':response_pay})
            
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request,'booking.html', dict_form)










def payment_status(request):
    response = request.POST
    client = razorpay.Client(auth=("rzp_test_BJzMHCR6f7fAac","QZzBZWbmbNnihxu5XM17tyA1"))
    try:
        status = client.utility.verify_payment_signature({
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
            })
        
        booking = Booking.objects.get(order_id=response['razorpay_order_id'])
        booking.razorpay_id = response['razorpay_payment_id']
        booking.pay_status = True
        booking.save()
        return render(request, 'confirm.html', {'status':True})
    except:
        return render(request, 'confirm.html', {'status':False})
        
    











def doctor(request):
    dict_docs={
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctor.html',dict_docs)

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'dept.html',dict_dept)

def contact(request):
    return render(request,'contact.html')