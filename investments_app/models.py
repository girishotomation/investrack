from django.db import models
from datetime import datetime

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User  # Use the default User model or your custom User model if you have one



PAYOUT_CHOICES = [
        ('MONTHLY', 'MONTHLY'),
        ('QUARTERLY', 'QUARTERLY'),
        ('HALF-YEARLY', 'HALF-YEARLY'),
        ('ANNUAL', 'ANNUAL'),
    ]


class Investment(models.Model):
    investment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    financial_institution = models.CharField(max_length=255)
    financial_product = models.CharField(max_length=255)
    investment_amount=models.FloatField(max_length=15,default=0)
    rate_of_interest =models.FloatField()
    interest_payout_frequency = models.CharField(choices=PAYOUT_CHOICES,max_length=255,default='ANNUAL')
    date_of_investment = models.DateField()
    date_of_maturity = models.DateField()
    crediting_bank_account = models.CharField(max_length=255)    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Investment {self.investment_id} by {self.user.username}"
    
    @property
    def isMaturing(self):
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%Y-%m")
        if  self.date_of_maturity.strftime("%Y-%m")==formatted_date:
            return True
            
