from rest_framework import viewsets, permissions 
from ..sources.models import Collection
from ..sources.serializer import CollectionListSerializer
from rest_framework.response import Response

from util.cache import cache_by_kwargs


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CollectionListSerializer

    @cache_by_kwargs(60*60*24)
    def list(self, request):
        query = request.query_params["query"]
        collections = Collection.objects.filter(name__icontains=query)
        # collections = [collection for collection in collections_query]
        # print(collections)
        serializer = CollectionListSerializer({'collections':collections})
        return Response(serializer.data)
