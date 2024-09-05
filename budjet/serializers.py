from .models import Budejet, Title
from rest_framework.serializers import ModelSerializer
class BudjetSerializer(ModelSerializer):
    class Meta:
       model = Budejet
       fields = "__all__"

class TitleSerializer(ModelSerializer):
    class Meta:
       model = Title
       fields = "__all__"    
