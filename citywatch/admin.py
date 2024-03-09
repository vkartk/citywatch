from django.contrib import admin

# Register your models here.

from .models import Issue, IssueCategory, IssueComment

admin.site.register(Issue)
admin.site.register(IssueCategory)
admin.site.register(IssueComment)