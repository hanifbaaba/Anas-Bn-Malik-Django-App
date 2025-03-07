from django.db import models

class Beneficiary(models.Model):
    name = models.CharField(max_length=255)  
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state_of_origin = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)  
    account_number = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nin_number = models.CharField(max_length=20, unique=True)
    administrator_name = models.CharField(max_length=255, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=100, blank=True, null=True)
    payment_officer = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    # gender = models.CharField(max_length=50, blank=True, null=True)  
    # need = models.CharField(max_length=255, blank=True, null=True)  
    # occupation = models.CharField(max_length=255, blank=True, null=True)  



    def __str__(self):
        return self.name
