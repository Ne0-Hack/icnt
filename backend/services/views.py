from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Order, Service
from .serializer import OrderReadSerializer, OrderCreateSerializer, ServiceReadSerializer


class OrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderReadSerializer

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)

    def create(self, request, *args, **kwargs):
        self.serializer_class = OrderCreateSerializer
        data = request.data
        data['customer'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceReadSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        print(self.request.query_params)
        if 'l' in self.request.query_params is not None:
            queryset = self.queryset.all()
            if 'e' in self.request.query_params is not None:
                queryset = queryset.exclude(id=self.request.query_params['e'])

            queryset = queryset[:int(self.request.query_params['l'])]

            print(queryset)
            return queryset
        return self.queryset
