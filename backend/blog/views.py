from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from blog.models import Article, Categories, Difficulties
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import ArticleSerializer, CategoriesSerializer, ArticleCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArticleAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'previous_page_number': self.previous_page_number(),
            'current_page_number': self.page.number,
            'next_page_number': self.next_page_number(),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

    def previous_page_number(self):
        current_page_number = self.page.number

        if current_page_number > 1:
            return current_page_number - 1
        return None

    def next_page_number(self):
        current_page_number = self.page.number
        total_pages = self.page.paginator.num_pages

        if total_pages > current_page_number:
            return current_page_number + 1
        return None


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = ArticleAPIListPagination


class ArticleAPICreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer






class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )




class ArticleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly, )


class ArticleAPIFilter(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = ArticleAPIListPagination
    # permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self, *args, **kwargs):
        filter_word = self.kwargs.get('filter')
        category = Categories.objects.get(slug=filter_word)
        return Article.objects.filter(category=category)


class CategoriesAPIList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesAPIRetrieve(generics.RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer





@api_view(['GET'])
def blog_list(request):
    if request.method == 'GET':
        blog = Article.objects.all()
        serializer = ArticleSerializer(blog, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def blog_post(request):
    if request.method == 'POST':

        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'theme': Categories.objects.get(theme=request.data.get('theme')),
            'difficulty': Difficulties.objects.get(difficulty=request.data.get('difficulty')),
        }
        blog = Article.objects.create(**data)
        serializer = ArticleSerializer(blog, many=True)
        return Response(blog)

