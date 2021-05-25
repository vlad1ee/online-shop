from rest_framework import generics, permissions
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model


User = get_user_model()


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
