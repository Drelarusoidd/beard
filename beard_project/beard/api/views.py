from rest_framework.views import Response, APIView
from .serializers import CommentSerializer, UserSerializer, AlbumSerializer, PhotoSerializer, TodoSerializer, PostsSerializer
from .models import Album, Todo, User, Comment, Photo, Post


class UsersView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentsView(APIView):

    def get(self, request):
        try:
            param = request.GET.get('postId', '')
            queryset = Comment.objects.filter(postId_id=param)
        except BaseException:
            queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


class AlbumsView(APIView):

    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)


class PhotosView(APIView):

    def get(self, request):
        queryset = Photo.objects.all()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)


class TodosView(APIView):

    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)


class PostsView(APIView):

    def get(self, request, slug=False):
        if slug and request.path.split('/')[-1] == 'comments':
            comments = Comment.objects.filter(postId=slug)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif slug:
            posts = Post.objects.get(pk=slug)
            serializer = PostsSerializer(posts)
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = PostsSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request):
        try:
            userId = request.GET.get('userId', '')
            title = request.GET.get('title', '')
            body = request.GET.get('body', '')
            count = Post.objects.all()[::-1][0].id
            Post.objects.create(userId_id=userId, title=title, body=body)
            return Response({'id': count + 1})
        except BaseException:
            return Response({})

    def put(self, request, slug):
        try:
            body = request.GET.get('body', '')
            Post.objects.filter(pk=slug).update(body=body)
            return Response({'body': body})
        except BaseException:
            return Response({'error': "This post doesn't exist"})

    def patch(self, request, slug):
        try:
            body = request.GET.get('body', '')
            Post.objects.filter(pk=slug).update(body=body)
            post = Post.objects.get(body=body)
            serializer = PostsSerializer(post)
            return Response(serializer.data)
        except BaseException:
            return Response({'error': "This post doesn't exist"})

    def delete(self, request, slug):
        try:
            Post.objects.get(pk=slug).delete()
        except BaseException:
            return Response({'error': "This pos doesn't exist"})
        return Response({})
