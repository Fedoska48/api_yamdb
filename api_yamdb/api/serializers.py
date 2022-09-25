from titles.models import Category, Genre, Title
from rest_framework import serializers

class TitleSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Category.objects.all())
    genre = serializers.ChoiceField(choices=Genre.objects.all())

    class Meta:
        fields = '__all__'
        model = Title


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category
