from django.urls import path
from blog.views import *


urlpatterns = [
    path('', ArticleAPIList.as_view()),
    path('create/', ArticleAPICreate.as_view()),
    path('<int:pk>/', ArticleAPIDetail.as_view()),
    path('update/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('delete/<int:pk>/', ArticleAPIDestroy.as_view()),
    path('filter=<str:filter>/', ArticleAPIFilter.as_view()),

    path('difficulties/', DifficultiesAPIList.as_view()),
    path('categories/', CategoriesAPIList.as_view()),
    path('categories/<int:pk>/', CategoriesAPIRetrieve.as_view()),
]
