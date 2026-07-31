from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display="name","email","hire_date","position","is_promo"
    list_display_links="name","email"
    list_editable="position","is_promo"
    search_fields="name",
    list_per_page=25

admin.site.register(Staff, StaffAdmin)