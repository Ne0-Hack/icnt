from rest_framework import serializers
from .models import CustomUser, country_list
from services.models import Order
from services.serializer import OrderReadSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'login', 'first_name', 'last_name', 'user_photo', 'age']


class UserFetchSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'login', 'first_name', 'last_name', 'user_photo', 'age', 'country', 'email', 'phone', 'orders']

    def get_orders(self, obj):
        queryset = Order.objects.filter(customer_id=obj.id)
        return OrderReadSerializer(queryset, many=True).data

    def get_country(self, obj):
        return country_list[int(obj.country)][1]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['login', 'first_name', 'last_name', 'password', 'email', 'phone', 'country', 'age']
