from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from .serializer import UserFetchSerializer, UserCreateSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.core.files.storage import default_storage

class UserViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserFetchSerializer

    def list(self, request, *args, **kwargs):
        user_profile = get_object_or_404(CustomUser, pk=request.user.id)
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(**serializer.data)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response(serializer.errors, status=400)

    def update(self, request, *args, **kwargs):
        file = request.data['image']
        file_name = default_storage.save(file.name, file)
        CustomUser.objects.filter(id=request.user.id).update(user_photo=file_name)
        return Response(status=201)
