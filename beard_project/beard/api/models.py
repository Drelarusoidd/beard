from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    catchPhrase = models.CharField(max_length=300)
    bs = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Geo(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=4)
    lng = models.DecimalField(max_digits=10, decimal_places=4)


class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=300)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', 'name']

    def __str__(self):
        return self.name


class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    completed = models.CharField(max_length=5)


class Album(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)


class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    url = models.URLField(default='http://placebeard.it/640/480/notag')
    thumbnailURL = models.URLField(default='http://placebeard.it/640/480/notag')


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    body = models.TextField()


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
