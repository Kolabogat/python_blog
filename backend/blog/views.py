from rest_framework import generics
from rest_framework import permissions

from blog.models import Article, Categories, Difficulties
from blog.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from blog.serializers import ArticleSerializer, CategoriesSerializer, ArticleCreateSerializer, DifficultiesSerializer
from blog.utils import ArticleAPIListPagination


class ArticleAPIList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleAPIListPagination


class ArticleAPICreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    # permission_classes = (permissions.IsAuthenticated, )


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ArticleAPIDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ArticleAPIFilter(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = ArticleAPIListPagination

    def get_queryset(self, *args, **kwargs):
        filter_word = self.kwargs.get('filter')
        return Article.objects.filter(category__slug=filter_word)


class DifficultiesAPIList(generics.ListAPIView):
    queryset = Difficulties.objects.all()
    serializer_class = DifficultiesSerializer


class CategoriesAPIList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesAPIRetrieve(generics.RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
