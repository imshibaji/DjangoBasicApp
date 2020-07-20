from django.contrib import admin

from .models import Contact

# Register your models here.

admin.site.site_header = "My Admin Central"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_time']


admin.site.register(Contact, ContactAdmin)