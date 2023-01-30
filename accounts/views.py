from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Accounts"],
)
class RegisterView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    @extend_schema(description="Listagem de contas")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Criação de conta")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
