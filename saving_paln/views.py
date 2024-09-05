from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
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
