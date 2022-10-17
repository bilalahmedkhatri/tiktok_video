from dataclasses import fields
from select import select
from video_editor.models import VideoOwner
from rest_framework import serializers


class OwnerSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = VideoOwner
        fields = ['id', 'owner_id', 'name', 'total_videos', 'created_at', 'updated_at']