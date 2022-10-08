from django.contrib import admin
from video_editor.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'age', 'status')
    
    
admin.site.register(Todo, TodoAdmin)