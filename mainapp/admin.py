from django.contrib import admin
from mainapp.models import Story,Comment,Watch


# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Watch)