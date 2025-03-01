from django.urls import path
from .views import BeneficiaryListCreateView, BeneficiaryRetrieveUpdateDeleteView

urlpatterns = [
    path('beneficiaries/', BeneficiaryListCreateView.as_view(), name='beneficiary-list'),
    path('beneficiaries/<int:pk>/', BeneficiaryRetrieveUpdateDeleteView.as_view(), name='beneficiary-detail'),
]
