from django.shortcuts import render
from rest_framework import generics
from .models import Beneficiary
from .serializers import BeneficiarySerializer



class BeneficiaryListCreateView(generics.ListCreateAPIView):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

class BeneficiaryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer


def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True  
        return self.update(request, *args, **kwargs)


