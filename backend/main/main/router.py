from rest_framework import routers
from api.viewsets import TodoItemViewset
from api.viewsets import TodoListViewset

router = routers.DefaultRouter()
router.register('todolists', TodoListViewset)
router.register('todos', TodoItemViewset)