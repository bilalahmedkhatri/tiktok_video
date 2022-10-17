from django.contrib import admin
from video_editor.models import HashTag, Todo, VideoID, VideoOwner
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'age', 'status']
    
@admin.register(VideoOwner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_id', 'name', 'total_videos', 'created_at', 'updated_at']
    list_display_link = ['owner_id', 'name']
    
@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'hashtag', 'count_hashtag', 'top_hashtag', 'count_top_tag_list', 'created_at', 'updated_at']
    list_display_link = ['hashtag', 'count_hashtag']

@admin.register(VideoID)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_id', 'owner_id', 'video_hashtags', 'created_at', 'updated_at']
    list_display_link = ['video_id', 'owner_id', 'video_hashtags']
    


