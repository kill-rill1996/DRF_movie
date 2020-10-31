from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Actor
from .serializers import (
    ActorDetailSerializer,
    ActorListSerializer,
)


# class ActorViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Actor.objects.all()
#         serialier = ActorListSerializer(queryset, many=True)
#         return Response(serialier.data)
#
#     def retrieve(self, request, pk):
#         queryset = Actor.objects.all()
#         actor = get_object_or_404(queryset, pk=pk)
#         serializer = ActorDetailSerializer(actor)
#         return Response(serializer.data)


# class ActorReadOnly(viewsets.ReadOnlyModelViewSet):
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer
#
#
# class ActorModelViewSet(viewsets.ModelViewSet):
#     serializer_class = ActorListSerializer
#     queryset = Actor.objects.all()
#
#
#
# @action(detail=True, methods=['get', 'put']) #, renderer_classes=[renderers.AdminRenderer])
# def example(self, request, *args, **kwargs):
#     actor = self.get_object()
#     serializer = ActorDetailSerializer(actor)
#     return Response(serializer.data)
#



