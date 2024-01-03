from rest_framework import serializers
from investments_app.models import Investment
from django.contrib.auth.models import User 

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'
        read_only_fields = ('investment_id', 'user', 'created_date', 'updated_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
