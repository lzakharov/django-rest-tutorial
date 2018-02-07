from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class GenericSnippetView():
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetList(GenericSnippetView, ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """


class SnippetDetail(GenericSnippetView, RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
