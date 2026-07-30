from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display="name","email","hire_date","position"
    list_display_links="name","email"
    list_editable="position",
    search_fields="name",
    list_per_page=25

admin.site.register(Staff, StaffAdmin)