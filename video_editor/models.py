from email.policy import default
from importlib.util import set_loader
from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Todo(models.Model):
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    