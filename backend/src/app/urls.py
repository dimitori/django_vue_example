from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from articles.api.v1.views import ArticleView


router = routers.DefaultRouter()
router.register('articles', ArticleView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
