from django.urls import path, re_path
from blog.views import *


urlpatterns = [
    path('blog_list/', ArticleAPIList.as_view()),
    path('blog_create/', ArticleAPICreate.as_view()),
    path('blog/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('blog_delete/<int:pk>/', ArticleAPIDestroy.as_view()),
    path('blog/?category=<str:category>/', ArticleAPIFilter.as_view()),

    path('categories/', CategoriesAPIList.as_view()),
    path('categories/<int:pk>/', CategoriesAPIRetrieve.as_view()),
]
