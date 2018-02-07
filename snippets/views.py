from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import StaticHTMLRenderer
from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class GenericUserView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(GenericUserView, ListCreateAPIView):
    """
    List all users, or create a new user.
    """


class UserDetail(GenericUserView, RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """


class GenericSnippetView(GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SnippetList(GenericSnippetView, ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(GenericSnippetView, RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
