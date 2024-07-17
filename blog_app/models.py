from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    job = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
