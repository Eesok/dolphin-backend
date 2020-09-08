from rest_framework import serializers
from .models import Item, Detail, Category


class CategorySerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('title', 'items',)


class ItemSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        read_only=True,

    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category_id'

    )

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'category', 'category_id',)


class DetailSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        read_only=True,

    )
    item = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        source='item_id'

    )

    class Meta:
        model = Detail
        fields = ('measurements', 'item', 'materials',
                  'styles', 'brand', 'item_id',)
