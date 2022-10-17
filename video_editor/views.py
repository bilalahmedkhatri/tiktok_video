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
from video_editor.serializer.video_owner import OwnerSerializers

# models
from video_editor.models import VideoOwner
from video_editor.models import VideoID
from video_editor.models import HashTag
from video_editor.models import Todo

# default python packages
import os
from subprocess import call


def test_index(requests):
    return HttpResponse('success')


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # permission_class = [permissions.AllowAny]


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def save_hashTags(request):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializers(queryset, many=True)
    x = os.getcwd()+"\\video_editor\hashtag.py"
    # x = os.getcwd()+"\\tiktok\hashtag.py"
    call(["py", x])
    # Popen(['gnome-terminal', '-e', 'echo "Hello World"'], stdout=PIPE)
    return Response(serializer_class.data)


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def hash_tag(request):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializers(queryset, many=True)
    # b = save_hashtag()
    b = on_connect()
    print('bilal', b)
    return Response(serializer_class.data)


