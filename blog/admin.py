from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # to get the slug field prepopulated with part of title
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title','slug','status','created_on')
    search_fields = ['title','content']
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name','email','body']
    # to provide an action that lets us approve a comment
    # actions takes a list of methods
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)