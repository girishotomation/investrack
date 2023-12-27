from django.contrib import admin
from investments_app import models
# Register your models here.

@admin.register(models.Investment)
class MyInvestments(admin.ModelAdmin):
    list_display=('investment_id','user','financial_product','rate_of_interest','interest_payout_frequency','date_of_investment','date_of_maturity','crediting_bank_account','created_date','updated_date')

    """
        investment_id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)    
        financial_product = models.CharField(max_length=255)
        rate_of_interest =models.IntegerField()
        interest_payout_frequency = models.CharField(choices=PAYOUT_CHOICES,max_length=255)
        date_of_investment = models.DateField()
        date_of_maturity = models.DateField()
        crediting_bank_account = models.CharField(max_length=255)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
    """

# Register your models here.
