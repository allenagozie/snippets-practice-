from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from snippet import views
from snippet.views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
	path('', include(router.urls)),
]