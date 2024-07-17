from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Category, Tag, Author, Article
from .serializers import CategorySerializer, TagSerializer, AuthorSerializer, ArticleSerializer
from .pagination import ArticlePagination
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ViewSet):
    queryset = Tag.objects.all()

    def list(self, request):
        serializer = TagSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        tag = get_object_or_404(self.queryset, pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def update(self, request, pk=None):
        tag = get_object_or_404(self.queryset, pk=pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        tag = get_object_or_404(self.queryset, pk=pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(viewsets.ViewSet):
    queryset = Author.objects.all()

    def list(self, request):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def update(self, request, pk=None):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        author = get_object_or_404(self.queryset, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleViewSet(viewsets.ViewSet):
    queryset = Article.objects.all()
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title', 'content']

    def list(self, request):
        queryset = self.queryset
        paginator = self.pagination_class()
        queryset = self.filter_queryset(queryset)
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ArticleSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
