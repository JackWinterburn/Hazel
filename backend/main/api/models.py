from django.db import models

# Create your models here.

class TodoItem(models.Model):
  title = models.CharField(max_length=35, null=False)
  description = models.TextField(null=False)
  start_date = models.DateTimeField(auto_now_add=True, auto_now=False)
  color = models.CharField(max_length=7, null=False)
  end_date = models.CharField(max_length=10)

  