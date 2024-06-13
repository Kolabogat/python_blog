from rest_framework import serializers

from blog.models import Article, Categories, Difficulties


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'category', 'slug')


class DifficultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulties
        fields = ('id', 'difficulty', 'class_name')


class ArticleSerializer(serializers.ModelSerializer):
    words_number = serializers.HiddenField(default=0)
    user = serializers.CharField(read_only=True)

    category = CategoriesSerializer(read_only=True)
    category_id = serializers.SlugRelatedField(queryset=Categories.objects.all(), slug_field='category', write_only=True)

    difficulty = DifficultiesSerializer(read_only=True)
    difficulty_id = serializers.SlugRelatedField(queryset=Difficulties.objects.all(), slug_field='difficulty', write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'user',
            'title',
            'image',
            'content',
            'words_number',
            'category',
            'category_id',
            'difficulty',
            'difficulty_id',
            'created_at',
        )


class ArticleCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'user',
            'title',
            'image',
            'content',
            'category',
            'difficulty',
        )


