from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from video_editor.serializer.todo import TodoSerializer

from video_editor.models import Todo
# Create your views here.


def test_index(requests):
    return HttpResponse('success')
    
    
class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_class = [permissions.AllowAny]