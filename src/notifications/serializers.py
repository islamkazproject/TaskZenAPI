from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Notification serializer"""

    class Meta:
        model = Notification
        exclude = ('task',)


class CreateNotificationSerializer(serializers.ModelSerializer):
    """Create Notification"""

    class Meta:
        model = Notification
        fields = ('task', 'name', 'launch_time',)

    def create(self, validated_data):
        instance_notification = super(CreateNotificationSerializer, self).create(validated_data)
        create_periodic_task(instance_notification)


class UpdateNotificationSerializer(serializers.ModelSerializer):
    """Update Notification"""

    class Meta:
        model = Notification
        fields = ('title', 'launch_time',)
