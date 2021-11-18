from django.contrib import admin
from django.utils.html import format_html
from .models import Enter_Detail

class Enter_DetailAdmin(admin.ModelAdmin):

    list_display  = ['name', 'reg', 'subject', 'mark']
    search_fields = ['name', 'reg']

admin.site.register(Enter_Detail, Enter_DetailAdmin)

# class NameAdmin(admin.ModelAdmin):

#     list_display = ['name']
#     search_fields = ['name']

# admin.site.register(Name, NameAdmin)

# class MarkAdmin(admin.ModelAdmin):

#     list_display = ['mark']
#     search_fields = ['mark']

# admin.site.register(Mark, MarkAdmin)