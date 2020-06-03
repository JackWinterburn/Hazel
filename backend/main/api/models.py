from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class TodoList(models.Model):
  name = models.CharField(max_length=32)


class TodoItem(models.Model):
  id
  title = models.CharField(max_length=40, null=False)
  description = models.TextField(null=False)
  color = models.CharField(max_length=7)
  start_date = models.DateTimeField(auto_now_add=True, auto_now=False)
  end_date = models.CharField(max_length=10)
  associated_list = models.ForeignKey('TodoList', on_delete=models.CASCADE)

  def __str__(self):
    return self.title
