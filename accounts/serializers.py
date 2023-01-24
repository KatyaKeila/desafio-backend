from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Account.objects.all())],
    )

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_superuser(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
