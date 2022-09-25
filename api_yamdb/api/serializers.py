from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Comment, Review
from titles.models import Category, Genre, Title


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


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.ReadOnlyField(
        source='review.id'
    )

    class Meta:
        fields = '__all__'
        model = Comment
