from dataclasses import field
from video_editor.models import HashTag
from rest_framework import serializers


class HashTagSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = HashTag
        fields = ['id', 'hashtag', 'count_hashtag', 'top_hashtag', 'count_top_tag_list', 'created_at', 'updated_at']