from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer создания нового пользователя."""

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                "Использовать имя 'me' в качестве username запрещено!"
            )
        return data


class CreateTokenSerializer(serializers.ModelSerializer):
    """Serializer создания токена для нового пользователя."""
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)
