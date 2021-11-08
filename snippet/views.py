from snippet.models import Snippet
from rest_framework import renderers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from snippet.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from snippet.serializers import SnippetSerializer, UserSerializer





class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	queryset = Snippet.object.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)