from django.db import models


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'labels'
    
    def __str__(self):
        return self.name