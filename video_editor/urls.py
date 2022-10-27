from django.urls import path
from video_editor.views import TodoView
from video_editor.views import hello_world
from video_editor.views import get_hashTags

urlpatterns = [
    path('hello-world/', hello_world, name='world'),
    path('hashtag/', get_hashTags, name='hashtag'),
]
