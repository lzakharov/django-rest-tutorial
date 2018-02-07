from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class GenericSnippetView(GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  GenericSnippetView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericSnippetView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
