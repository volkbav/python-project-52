from django.db import models
from django.contrib.auth.models import User
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
#        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
#        null=True
    )
    
 #   class Meta:
 #       verbose_name_plural = 'tasks'
    def __str__(self):
        return self.name