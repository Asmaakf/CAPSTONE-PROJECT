from django.contrib import admin
from .models import Attachment
# Register your models here.
class AttachmentAdmin(admin.ModelAdmin):
    list_display=['title','media','group','uploaded_by','uploaded_at']
admin.site.register(Attachment,AttachmentAdmin)
