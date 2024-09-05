from .models import Transaction, Totalbalance
from rest_framework import serializers

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class TotalbalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totalbalance
        fields = "__all__"