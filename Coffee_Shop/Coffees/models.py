from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class CoffeeTypes(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(null=False)
    price = models.IntegerField(max_length=10)
    image = models.ImageField(upload_to='imgs/', null=False)

    def __str__(self):
        return self.name

class EmployeesData(models.Model):
    EMP_ROLE = [
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=25,null=False)
    last_name = models.CharField(max_length=25,null=False)
    email = models.EmailField(null=False)
    mobile_no = models.IntegerField(max_length=10,null=False)
    profile = models.ImageField(upload_to='profiles/',null=False)
    role = models.CharField(choices=EMP_ROLE,null=False)

    def __str__(self):
        return self.last_name
    
class Users(models.Model):
    name = models.CharField(max_length=25,null=False)
    email = models.EmailField(null=False)
    mobile_no = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be exactly 10 digits."
            )
        ]
    )
    message = models.TextField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_TYPE = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='User')
    coffee = models.ForeignKey(CoffeeTypes, on_delete=models.CASCADE, related_name='order_items')
    order_date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    status = models.CharField(max_length=20,choices=STATUS_TYPE,default='Pending')

    def __str__(self):
        return f"{self.user.name}"
    
class Payments(models.Model):
    PAYMENT_STATUS =[
        ('Pending','Pending'),
        ('paid','Paid'),
        ('Failed','Failed')
    ]
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='user_payment')
    ammount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS)
    payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.Order.user.name}"