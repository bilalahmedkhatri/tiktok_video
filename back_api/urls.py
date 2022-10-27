from django.contrib import admin
from django.urls import path, include
from video_editor.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'video_editor'), namespace='video_editor')),
    path("", include('video_editor.urls'))
]
