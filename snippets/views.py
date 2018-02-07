from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer


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
