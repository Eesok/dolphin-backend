from rest_framework import serializers
from .models import Item, Detail, Category


class CategorySerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'title', 'items', 'category_image')


class ItemSerializer(serializers.ModelSerializer):
    # category_id = serializers.PrimaryKeyRelatedField(
    #     read_only=True,

    # )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        # source='category_id'

    )
    details = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description',
                  'category', 'details', 'item_photo',)


class DetailSerializer(serializers.ModelSerializer):
    # item_id = serializers.PrimaryKeyRelatedField(
    #     read_only=True,

    # )
    item = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        # source='item_id'

    )

    class Meta:
        model = Detail
        fields = ('id', 'measurements', 'item', 'materials',
                  'styles', 'brand',)
