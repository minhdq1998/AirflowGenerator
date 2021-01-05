from django.contrib import admin

from .models import Task, S3ToGoogleCloudStorageTask, DummyTask, DagFile

admin.site.register(DagFile)
admin.site.register(DummyTask)
admin.site.register(S3ToGoogleCloudStorageTask)
