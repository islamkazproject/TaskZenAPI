from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Category Title', unique=True)
    description = models.CharField(max_length=255, verbose_name='Category Description', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Category Created At')

    class Meta:
        verbose_name_plural = "Task Categories"

    def __str__(self):
        return f'{self.title} - {self.description}'


class Label(models.Model):
    title = models.CharField(max_length=50, verbose_name='Label Title', null=True, unique=True)
    description = models.CharField(max_length=255, verbose_name='Label Description', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Label Created At', null=True)

    def __str__(self):
        return f'{self.title} - {self.description}'


class Attachment(models.Model):
    filename = models.CharField(max_length=255, verbose_name='Attachment Filename', null=True, unique=True)
    file = models.FileField(upload_to='attachments/', verbose_name='Attachment File', null=True)
    filetype = models.CharField(max_length=50, verbose_name='Attachment Filetype', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Attachment Created At', null=True)

    def __str__(self):
        return f'{self.filename}'


class Task(models.Model):
    STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
        ('DELEGATED', 'Delegated')
    ]

    title = models.CharField(max_length=100, verbose_name='Task Title')
    description = models.TextField(blank=True, null=True, verbose_name='Task Description')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Task Category',
        related_name='categories',
        blank=True,
        null=True
    )
    label = models.ForeignKey(
        'Label',
        on_delete=models.SET_NULL,
        verbose_name='Task Label',
        related_name='labels',
        blank=True,
        null=True
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Assigned To',
        related_name='assigned_to',
    )
    attachments = models.ForeignKey(
        'Attachment',
        on_delete=models.SET_NULL,
        verbose_name='Task Attachments',
        related_name='attachments',
        blank=True,
        null=True
    )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='TO_DO', verbose_name='Task Status')
    priority = models.CharField(
        max_length=10,
        choices=(('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')),
        default='LOW',
        verbose_name='Task Priority'
    )
    due_date = models.DateField(null=True, blank=True, verbose_name='Due Date')
    start_time = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name='Start Time')
    end_time = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name='End Time')
    comments = models.TextField(blank=True, null=True, verbose_name='Task Comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Task Created At')

    class Meta:
        ordering = ["-created_at"]  # сортировка дел по времени их создания

    def __str__(self):
        return (f'{self.category} '
                f'{self.title} '
                f'{self.description} '
                f'{self.assigned_to} '
                f'{self.status} '
                f'{self.priority}')


class Subtask(models.Model):
    parent_task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks',
        verbose_name='Parent Task',
        to_field='id',
    )
    subtask_title = models.CharField(max_length=100, verbose_name='Subtask Title')
    subtask_description = models.TextField(verbose_name='Subtask Description', blank=True)
    subtask_completed = models.BooleanField(verbose_name='Subtask Completed', default=False)
    subtask_comment = models.TextField(verbose_name='Subtask Comment', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Subtask Created At')

    def __str__(self):
        return (f'{self.parent_task.category.title} - {self.parent_task.title} '
                f'{self.subtask_title} '
                f'{self.subtask_description} '
                f'{self.subtask_completed} '
                f'{self.subtask_comment} ')
