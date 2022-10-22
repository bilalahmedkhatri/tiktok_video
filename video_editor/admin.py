from django.contrib import admin
from video_editor.models import HashTag, Todo, VideoID, VideoAuthor
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'age', 'status']
    
@admin.register(VideoAuthor)
class authorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'name', 'total_videos', 'count_videos', 'followers', 'created_at', 'updated_at']
    list_display_link = ['author_id', 'name']
    
@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'hashtag', 'count_hashtag', 'top_hashtag', 'count_top_tag_list', 'created_at', 'updated_at']
    list_display_link = ['hashtag', 'count_hashtag']
    search_fields = ['hashtag']

@admin.register(VideoID)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_id', 'author_id', 'len_hashtags', 'video_hashtags', 'created_at', 'updated_at']
    list_display_link = ['video_id', 'author_id', 'video_hashtags']
    search_fields = ['author_id__name', 'len_hashtags',]
    


