from django.urls import path
from authors.views import authors

urlpatterns = [
    path('authors', authors)
]
