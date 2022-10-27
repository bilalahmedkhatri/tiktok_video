from django.http import HttpResponse
from django.shortcuts import render

#rest Framework
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

# Serializers
from video_editor.serializer.todo import TodoSerializer
from video_editor.serializer.hashtag import HashTagSerializers
from video_editor.serializer.video_id import VideoSerializers
from video_editor.serializer.video_author import AuthorSerializers

# models
from video_editor.models import VideoAuthor
from video_editor.models import VideoID
from video_editor.models import HashTag
from video_editor.models import Todo

# default python packages
from subprocess import call


def test_index(requests):
    return HttpResponse('success')


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    x = viewsets
    print(dir(x))
    # permission_class = [permissions.AllowAny]


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_hashTags(request):
    queryset = HashTag.objects.all().order_by('id')[:10]
    serializer_class = HashTagSerializers(queryset, many=True)
    return Response(serializer_class.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def hash_tag(request):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializers(queryset, many=True)
    return Response(serializer_class.data)


# only read data
class HashTagReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HashTagSerializers
    queryset = HashTag.objects.all()
    
    
# Just test for reouting porpuse
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all()
    
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)