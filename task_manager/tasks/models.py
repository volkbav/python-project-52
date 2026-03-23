# task_manager/tasks/models.py
from django.contrib.auth.models import User
from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.projects.models import Project


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author_tasks',
        blank=False,
        null=False,
    )
    executor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks_executor',
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='tasks_projects',
    )
    
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=False,
        related_name='tasks',
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
        