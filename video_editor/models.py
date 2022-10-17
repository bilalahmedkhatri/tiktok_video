from contextlib import nullcontext
from email.headerregistry import UniqueSingleAddressHeader
from email.policy import default
from enum import unique
from importlib.util import set_loader
from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todo(models.Model):
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class VideoOwner(models.Model):
    owner_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    total_videos = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class HashTag(models.Model):
    hashtag = models.CharField(max_length=256, unique=True)
    count_hashtag = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    top_hashtag = models.BooleanField(default=False, null=True, blank=True)
    count_top_tag_list = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self) -> str:   
        return self.hashtag
    
    
class VideoID(models.Model):
    video_id = models.BigIntegerField(unique=True)
    video_hashtags = models.ForeignKey(HashTag, verbose_name="Video tags", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(VideoOwner, verbose_name="Video Onwer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __int__(self) -> int:
        return self.video_id
    
    
    