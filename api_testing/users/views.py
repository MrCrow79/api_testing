from rest_framework import generics

from .models import User
from .serializer import UserSerializer

from .models import JobPosition
from .serializer import JobPositionSerializer


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobPositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobPositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
