from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = TodoItem
    fields = (
      'id',
      'title',
      'description',
      'start_date',
      'end_date',
      'color',
    )