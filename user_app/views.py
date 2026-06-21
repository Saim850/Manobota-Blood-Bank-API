from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserInformationsSerializer, DeleteUserSerializer
from user_app.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import serializers

class UserRegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "User registered successfully.",
                "user": serializer.data
            }, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

class UserInformationsViewSet(viewsets.ModelViewSet):
    serializer_class = UserInformationsSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).all()

class DeleteUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        object = get_object_or_404(User, email=email, phone_number=phone_number)

        if object:
            self.perform_destroy(object)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise serializers.ValidationError("!! Email and Phone Number dose not exists !!")
