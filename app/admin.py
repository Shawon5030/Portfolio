from django.contrib import admin
from .models import Coding_profile_detail

class CodingProfileDetailAdmin(admin.ModelAdmin):
    list_display = ['codeforces_rating', 'codechef_star', 'leetcode', 'total_problem_solved']
    search_fields = ['codeforces_rating', 'codechef_star', 'leetcode']

admin.site.register(Coding_profile_detail, CodingProfileDetailAdmin)


from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"