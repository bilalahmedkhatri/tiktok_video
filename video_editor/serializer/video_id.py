from dataclasses import field
import imp
from operator import imod
from video_editor.models import VideoID
from rest_framework import serializers


class VideoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = VideoID
        fields = ['id', 'video_id', 'owner_id', 'video_hashtags', 'created_at', 'updated_at']