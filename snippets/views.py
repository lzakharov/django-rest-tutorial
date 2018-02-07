from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer


class GenericUserView:
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


class GenericSnippetView:
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


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
