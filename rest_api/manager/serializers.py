from rest_framework import serializers
from .models import CustomUser
from .models import transact

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only':True}}

class transactSerializer(serializers.ModelSerializer):
    class Meta:
        model = transact
        fields = "__all__"
       