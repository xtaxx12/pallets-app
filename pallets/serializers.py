from rest_framework import serializers
from .models import Pallet

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = '__all__'
