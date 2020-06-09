from rest_framework import routers
from api.viewsets import TodoItemViewset

router = routers.DefaultRouter()
router.register('todos', TodoItemViewset)