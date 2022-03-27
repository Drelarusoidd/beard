from rest_framework import serializers
from .models import Company, User, Geo, Address, Comment, Photo, Album, Todo, Post


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        exclude = ['id']


class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        exclude = ['id']


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
