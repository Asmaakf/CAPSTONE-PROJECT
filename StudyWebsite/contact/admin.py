from django.contrib import admin
from .models import ContactSupport
# Register your models here.
class ContactSupportAdmin(admin.ModelAdmin):
    list_display=['name','email','message','msg_at']
admin.site.register(ContactSupport,ContactSupportAdmin)