from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Label, Attachment, Task, Subtask


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'created_at']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'title', 'description', 'created_at']


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'filename', 'file', 'filetype', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = [
            'id',
            'subtask_title',
            'subtask_description',
            'subtask_completed',
            'subtask_comment'
        ]


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    label = LabelSerializer()
    assigned_to = UserSerializer(read_only=True)
    attachments = AttachmentSerializer()
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id',
                  'title',
                  'description',
                  'category',
                  'label',
                  'assigned_to',
                  'attachments',
                  'status',
                  'priority',
                  'due_date',
                  'start_time',
                  'end_time',
                  'comments',
                  'created_at',
                  'subtasks'
                  ]
