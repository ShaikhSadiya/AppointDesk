from django.db import models
from  django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    status = models. CharField(
        max_length=20,
        choices= STATUS_CHOICES,
        default='Pending'
    )

    book_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.customer_name

