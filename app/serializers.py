from rest_framework import serializers
from .models import *


class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ['created_at', 'updated_at']