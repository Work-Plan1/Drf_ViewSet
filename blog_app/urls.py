from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, AuthorViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
