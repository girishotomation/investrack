from django.urls import path
from .views import InvestmentListCreateView, InvestmentDetailView,manage_investment

urlpatterns = [
    path('api/investments/', InvestmentListCreateView.as_view(), name='investment-list-create'),
    path('api/investments/<int:pk>/', manage_investment, name='investment-detail'),
]
