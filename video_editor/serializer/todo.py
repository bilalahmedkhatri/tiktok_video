from pyexpat import model
from rest_framework import serializers
from video_editor.models import Todo



class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ("first_name", "age", "status")