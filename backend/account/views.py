from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
