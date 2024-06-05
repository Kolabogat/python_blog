from django.urls import path
from blog.views import *


urlpatterns = [
    path('article/', ArticleAPIList.as_view()),
    path('article/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('article_delete/<int:pk>/', ArticleAPIDestroy.as_view()),
]
