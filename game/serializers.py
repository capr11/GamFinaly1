from rest_framework import serializers
from .models import Category, Image, Game

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
            'logo',
        )


class GameDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    images = ImageListSerializer(many=True)

    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
            'category',
            'logo',
            'images',
            'created_date',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file']

class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer(many=True)
    logo = serializers.ImageField(required=True)

    class Meta:
        model = Game
        fields = [
            'id', 'category', 'title', 'description', 'logo',
            'images', 'created_date', 'updated_date'
        ]
        read_only_fields = ['created_date', 'update_date']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')

        category, created = Category.objects.get_or_create(**category_data)
        game = Game.objects.create(category=category, **validated_data)

        for image_data in images_data:
            image = Image.objects.create(**image_data)
            game.images.add(image)

        return game

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        images_data = validated_data.pop('images', None)

        if category_data:
            category, created = Category.objects.get_or_create(**category_data)
            instance.category = category

        if images_data:
            instance.images.clear()
            for image_data in images_data:
                image = Image.objects.create(**image_data)
                instance.images.add(image)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        return instance


