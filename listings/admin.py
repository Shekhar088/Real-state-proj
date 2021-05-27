from django.contrib import admin
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'state', 'is_published' , 'realtor')
    list_display_links = ('id', 'title', 'realtor')
    list_filter = ('realtor', 'state')
    list_editable =('is_published',)
    search_fields = ('title', 'description', 'price', 'state', 'address', 'zipcode', 'city')
    list_per_page =20


admin.site.register(Listing, ListingAdmin)