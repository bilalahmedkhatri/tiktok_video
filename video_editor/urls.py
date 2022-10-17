from argparse import Namespace
from django.urls import path, include
from video_editor.views import TodoView, test_index, HashTagsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'run-test', HashTagsView, basename='hashtagview')


urlpatterns = [
    # path('', test_index, name="test-index"),
    
    # DRF login Logout more info check (" https://www.django-rest-framework.org/#installation ")
    path('', include(router.urls))
]