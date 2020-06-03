from rest_framework import serializers
from .models import TodoItem, TodoList

class TodoItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoItem
    fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoList
    fields = '__all__'
