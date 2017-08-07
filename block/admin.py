from django.contrib import admin
from block.models import Block
# Register your models here.

class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager")

admin.site.register(Block,BlockAdmin)
