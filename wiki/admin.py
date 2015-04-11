from django.contrib import admin
from wiki.models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date',]
    fieldsets = [
        (None,               {'fields': ['title', 'category']}),
        ('Content', {'fields': ['content']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('full_title', 'category', 'content', 'pub_date')
    list_filter = ['pub_date', 'category']
    search_fields = ['title', 'content', 'category']


admin.site.register(Page, PageAdmin)
