from .models import SavingPlan, TotalSaving
from rest_framework.serializers import ModelSerializer
class SavingPlanSerializer:
    class Meta:
        model = SavingPlan
        fieds = "__all__"

class TotalSavingSerializer:
    class Meta:
        model = TotalSaving
        fieds = "__all__"