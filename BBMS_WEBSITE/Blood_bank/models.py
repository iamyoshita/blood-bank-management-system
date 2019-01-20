from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Bank(models.Model):
    bank_id=models.CharField(max_length=100)
    #balance=models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=10)
    balance=models.PositiveIntegerField(default=0)
    password=models.CharField(max_length=30)

class Donor(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=15)
    locality=models.CharField(max_length=200)
    bank_id=models.ForeignKey(Bank,on_delete=models.CASCADE)
    blood_group=models.CharField(max_length=10)
    def __str__(self):
        return self.name + ": Donor; Blood group : " + self.blood_group
class Receiver(models.Model):
    name=models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    locality = models.CharField(max_length=200)
    bank_id = models.ForeignKey(Bank,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)


    def __str__(self):
        return self.name + ": Rceiver; Blood group : " + self.blood_group

"""class Bank(models.Model):
    bank_id=models.CharField(max_length=100)
    #balance=models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=10)
    balance=models.PositiveIntegerField(default=0)
    password=models.CharField(max_length=30)"""

class Staff(models.Model):
    name=models.CharField(max_length=100)
    salary=models.CharField(max_length=10)
    def __str__(self):
        return self.name +" Staff"

# Create your models here.
