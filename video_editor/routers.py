from video_editor.views import TodoView
from video_editor.views import HashTagReadOnlyModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'todo', TodoView, basename='todo')
router.register(r'hashtagsonly', HashTagReadOnlyModelViewSet, basename='hashtagsonly')

