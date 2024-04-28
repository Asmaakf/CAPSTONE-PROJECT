from django.contrib import admin
from .models import ReviewSet
# Register your models here.
class ReviewSetAdmin(admin.ModelAdmin):
    list_display=['title','description','group']
admin.site.register(ReviewSet,ReviewSetAdmin)
