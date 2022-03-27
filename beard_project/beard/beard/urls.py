"""beard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import UsersView, CommentsView, AlbumsView, PhotosView, TodosView
from api.views import PostsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UsersView.as_view(), name='users'),
    path('posts', PostsView.as_view(), name='list_posts'),
    path('posts/<slug>', PostsView.as_view(), name='posts_id'),
    path('posts/<slug>/comments', PostsView.as_view(), name='post_comments'),
    path('comments/', CommentsView.as_view(), name='comments'),
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('todos/', TodosView.as_view(), name='todos'),
]
