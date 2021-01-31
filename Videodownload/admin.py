from django.contrib import admin

# Register your models here.
from .models import contact,ads;

class AdminData(admin.ModelAdmin):
	list_display = ('Email', 'Name')
    
admin.site.register(contact, AdminData)
admin.site.site_header = "Download Videos" 
admin.site.register(ads)


