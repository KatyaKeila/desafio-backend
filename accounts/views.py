from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account

class RegisterView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()