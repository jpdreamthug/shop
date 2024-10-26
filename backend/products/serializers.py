from rest_framework import serializers

from products.models import Category, Tag, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'stock',
            'category', 'tags', 'created_at', 'updated_at',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'stock',
            'category', 'tags', 'created_at', 'updated_at',
        )
