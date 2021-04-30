from rest_framework import serializers
from . models import User, Elec_provider,User_electricity, Subscription
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='__all__'
class Elec_providerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Elec_provider
        fields = '__all__'
class User_electricitySerializer(serializers.ModelSerializer):
    class Meta:
        model= User_electricity
        fields = '__all__'
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subscription
        fields = '__all__'
