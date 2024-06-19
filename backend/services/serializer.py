from rest_framework import serializers
from .models import Order, OrderStatus, ServiceCategory, Service


class ServiceCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class ServiceReadSerializer(serializers.ModelSerializer):
    category_list = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image', 'image_card', 'category_list', 'slug']
        lookup_field = 'slug'

    def get_category_list(self, obj):
        category_list = ServiceCategory.objects.filter(service=obj)
        return ServiceCategoryReadSerializer(category_list, many=True).data


class OrderReadSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['service', 'customer', 'description', 'deadline', 'status']

    def get_status(self, obj):
        return OrderStatus[int(obj.status)]

    def get_service(self, obj):
        service = Service.objects.get(servicecategory=obj.serviceCategory).title
        category = obj.serviceCategory.title
        return [service, category]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['serviceCategory', 'customer', 'description', 'deadline']
