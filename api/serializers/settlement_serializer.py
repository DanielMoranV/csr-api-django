from rest_framework import serializers
from models import Settlement


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ['id', 'name', 'address', 'phone', 'email', 'website',
                  'description', 'image', 'created_at', 'updated_at']
