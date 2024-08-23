from django.contrib import admin
from . import models
# Register your models here.
class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ['id','todo','time']

admin.site.register(models.TodoModel, ToDoModelAdmin)



