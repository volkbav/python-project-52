from django.contrib.auth.models import User
from django.db import models

from task_manager.statuses.models import Status


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=False,
        related_name='tasks',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author_tasks',
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    executor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks_executor',
    )
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
        