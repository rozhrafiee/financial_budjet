from .models import SavingPlan, TotalSaving
from rest_framework.serializers import ModelSerializer
class SavingPlanSerializer:
    class Meta:
        model = SavingPlan
        fieds = "__all__"

     