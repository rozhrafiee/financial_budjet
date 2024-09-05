from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from .models import SavingPlan, TotalSaving
from .serializers import SavingPlanSerializer, TotalSavingSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, UpdateAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class SavingPlanList(ListCreateAPIView):
    queryset = SavingPlan.objects.all()
    serializer_class = SavingPlanSerializer 

class TotalSavingList(ListCreateAPIView):
    queryset = TotalSaving.objects.all()
    serializer_class = TotalSavingSerializer

class SavingPlanDetail(RetrieveUpdateDestroyAPIView):
    queryset = SavingPlan.objects.all()
    serializer_class = SavingPlanSerializer

class TotalSavingDetail(RetrieveUpdateDestroyAPIView):
    queryset = TotalSaving.objects.all()
    serializer_class = TotalSavingSerializer
    
def make_totel_saving(request):
    money = SavingPlan.monthly_saving *(SavingPlan.start_month -datetime)
    TotalSaving.totel_saving = money
    TotalSaving.totel_saving.save()
    
