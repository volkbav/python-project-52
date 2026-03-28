from datetime import date

from django.contrib.auth.models import User
from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='projects_author',
        blank=False,
        null=False,
    )
    executor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='projects_executor',
    )
    
    # foreing models
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=False,
        related_name='projects',
    )
    labels = models.ManyToManyField(
        Label,
        related_name='projects',
        blank=True,
    )

    start_date = models.DateField(
        default=date.today,
        help_text=(
            "Please use the following format: "
            "<em>YYYY-MM-DD</em>."
        ),
        null=True,
        blank=True,
    )
    deadline = models.DateField(
        help_text=(
            "Please use the following format: "
            "<em>YYYY-MM-DD</em>."
        ),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
