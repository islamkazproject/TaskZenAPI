from django.urls import include, path
from rest_framework import routers
from tasks.views import (
    AttachmentViewSet,
    CategoryViewSet,
    LabelViewSet,
    SubtaskViewSet,
    TaskViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'tasks/(?P<task_id>\d+)/subtasks', SubtaskViewSet, basename='subtasks')

urlpatterns = [
    path("", include(router.urls)),
]