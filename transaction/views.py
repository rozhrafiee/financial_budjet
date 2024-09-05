from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Companies, Totalbalance
from .serializers import CompaniesSerializer, TotalbalanceSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, UpdateAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class CompaniesList(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
class CompaniesCreate(CreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
class totalbalanceList(ListAPIView):
    queryset = Totalbalance.objects.all()
    serializer_class = TotalbalanceSerializer