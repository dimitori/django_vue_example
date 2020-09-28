from rest_framework import viewsets
from articles.api.v1.serializers import ArticleSerializer
from articles.models import Article


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

