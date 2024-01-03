from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
from .models import Investment


# Create your views here.
@login_required
def view_home(request):
    investment_data=Investment.objects.filter(user=request.user)     
    return render(request,'investments/home.html',{'investment_data':investment_data})   

@login_required
def view_home_drf(request):   
    api_url = "http://127.0.0.1:8000/api/investments/" 
    response = requests.get(api_url)
    investment_data = response.json() if response.status_code == 200 else []
    return render(request,'investments/home.html',{'investment_data':investment_data})


@login_required
def view_add_new_investment(request):
    if request.method=='POST':
        financial_product_dd=financial_institution= request.POST.get('financial_product_dd')
        financial_institution= request.POST.get('financial_institution')
        amount= request.POST.get('amount')
        rate_of_interest= request.POST.get('rate_of_interest')
        interest_payout_frequency= request.POST.get('interest_payout_frequency')
        date_of_investment= request.POST.get('date_of_investment')
        date_of_maturity= request.POST.get('date_of_maturity')
        crediting_bank_account= request.POST.get('crediting_bank_account')
        investment_obj = Investment(user=request.user,financial_institution=financial_institution,financial_product=financial_product_dd,investment_amount=amount,rate_of_interest=rate_of_interest,
                                    interest_payout_frequency=interest_payout_frequency,date_of_investment=date_of_investment,date_of_maturity=date_of_maturity,crediting_bank_account=crediting_bank_account)
        investment_obj.save()
        success_msg="Investment added successfully"
        return render(request,'investments/addinvestment.html',{'success_msg':success_msg})
    return render(request,'investments/addinvestment.html')


@login_required
def update_investment_view(request,pk):
    #record=get_object_or_404(Investment, pk=pk)    
    record=Investment.objects.get(investment_id=pk)   
    if request.method=='POST':
        record.financial_product=request.POST.get('financial_product_dd')
        record.financial_institution= request.POST.get('financial_institution')
        record.investment_amount= request.POST.get('amount')
        record.rate_of_interest= request.POST.get('rate_of_interest')
        record.interest_payout_frequency= request.POST.get('interest_payout_frequency')
        record.date_of_investment= request.POST.get('date_of_investment')
        record.date_of_maturity= request.POST.get('date_of_maturity')
        record.crediting_bank_account= request.POST.get('crediting_bank_account')
       # investment_obj = Investment(user=request.user,financial_institution=financial_institution,financial_product=financial_product_dd,rate_of_interest=rate_of_interest,
        #                            interest_payout_frequency=interest_payout_frequency,date_of_investment=date_of_investment,date_of_maturity=date_of_maturity,crediting_bank_account=crediting_bank_account)
        record.save()        
        update_success_msg="Investment UPDATED successfully"
        return render(request,'investments/updateinvestments.html',{'update_success_msg':update_success_msg})
    return render(request,'investments/updateinvestments.html',{'record':record})

@login_required
def delete_investment_view(request,pk):
    #record=get_object_or_404(Investment, pk=pk)    
    record=Investment.objects.get(investment_id=pk)   
    print(record)       
    record.delete()        
    delete_success_msg="Investment DELETED successfully"
    return render(request,'investments/home.html',{'delete_success_msg':delete_success_msg})
    




