from django.contrib import admin
from .models import *

admin.site.register(Post)

@admin.register(Comments)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active', 'created', 'body')
    search_fields = ('name', 'email','body')

