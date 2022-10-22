from dataclasses import fields
from select import select
from video_editor.models import VideoAuthor
from rest_framework import serializers


class AuthorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = VideoAuthor
        fields = ['id', 'owner_id', 'name', 'total_videos', 'created_at', 'updated_at']