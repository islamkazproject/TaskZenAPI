from django.contrib.auth.models import User
from django.db import models

from tasks.models import Task


class Notification(models.Model):
    class TaskType(models.TextChoices):
        TASK_CREATED = 'TASK_CREATED', 'Task Created'
        TASK_COMPLETED = 'TASK_COMPLETED', 'Task Completed'
        TASK_DELETED = 'TASK_DELETED', 'Task Deleted'

    task = models.OneToOneField(
        Task,
        verbose_name='Task',
        related_name='task_notifications',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(max_length=21, choices=TaskType.choices, default=TaskType.TASK_CREATED, verbose_name='Status')
    message = models.TextField(null=True, blank=True, verbose_name='Message')
    launch_time = models.DateTimeField(blank=True, null=True, verbose_name='Launch Time')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'{self.task} - {self.get_status_display()}'
