from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TitleSerializer
from .models import Title , Budejet
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView , token_refresh


class BudjetDetail(ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Title.objects.filter(user=self.request.user)



# Create your views here.
