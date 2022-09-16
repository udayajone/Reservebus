from django.contrib import admin
from ticketprocess.models import bus

class busadmin(admin.ModelAdmin):
    busdetails=["bus_name","route","start", "end","seats","balanseat","fare","date","time"]

admin.site.register(bus,busadmin)

# Register your models here.



