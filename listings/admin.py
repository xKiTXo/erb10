from django.contrib import admin
from .models import Listing, Menu
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from taggit.forms import TagWidget

class ListingAdminForm(forms.ModelForm):
    specialty = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='Specialty',is_stacked=False,attrs={'rows':'5'}),
        required=False,
        label="Food Specialties"
    )

    class Meta:
        model = Listing
        fields="__all__"
        widgets={
            "room_type":TagWidget(),
        }


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display="id","title","is_published","chef","list_date","display_specialty",'tag_list'
    list_display_links="id","title"
    list_filter="chef","list_date"
    list_editable="is_published",
    search_fields="title","description","district","specialty__food"
    list_per_page=25
    show_facets = admin.ShowFacets.ALWAYS

    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related('specialty','room_type')

    def display_specialty(self,obj):
        return ", ".join([specialty.food for specialty in obj.specialty.all()]) or 'None'
    
    display_specialty.short_description = "Specialty"
    form = ListingAdminForm


class MenuAdmin(admin.ModelAdmin):
    list_display="food",
    search_fields="food",

admin.site.register(Listing,ListingAdmin)
admin.site.register(Menu,MenuAdmin)
