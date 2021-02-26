from library.views import (CategoryViewSet,AuthorViewSet,BookViewSet)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'categorys', CategoryViewSet, basename='category')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls