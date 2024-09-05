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

class login(TokenObtainPairView):
    pass

class refresh(token_refresh):
    pass

def make_budjet(request):
    money = Title.budget - Title.payed_price
    Budejet.budjet = money
    Budejet.budjet.save()
    



# Create your views here.
