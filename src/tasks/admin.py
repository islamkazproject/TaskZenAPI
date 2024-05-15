from django.contrib import admin

from tasks.models import Task, Attachment, Subtask, Label, Category

# Register your models here.
admin.site.register(Task)
admin.site.register(Attachment)
admin.site.register(Subtask)
admin.site.register(Label)
admin.site.register(Category)
