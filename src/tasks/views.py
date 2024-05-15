from rest_framework import viewsets
from rest_framework.response import Response

from tasks.models import Attachment, Category, Label, Subtask, Task
from tasks.serializers import (
    AttachmentSerializer,
    CategorySerializer,
    LabelSerializer,
    SubtaskSerializer,
    TaskSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_subtasks(self, request, pk=None):
        task = self.get_object()
        subtasks = task.subtasks.all()
        serializer = SubtaskSerializer(subtasks)
        return Response(serializer.data)


class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Subtask.objects.filter(parent_task=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        serializer.save(parent_task=task)
