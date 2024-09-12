from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=500)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=500)
    doc_spec = models.CharField(max_length=500)
    doc_img = models.ImageField(upload_to='doctors')
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return 'Dr. ' + self.doc_name + ' (' + self.doc_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=500)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    book_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
