from django.urls import path
from blog.views import *


urlpatterns = [
    path('blogs/', ArticleAPIList.as_view()),
    path('blog/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('blog_delete/<int:pk>/', ArticleAPIDestroy.as_view()),
]
