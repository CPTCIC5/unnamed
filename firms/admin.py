from django.contrib import admin
from .models import Firm,Entity,FirmInvite
# Register your models here.
admin.site.register(Firm)
admin.site.register(FirmInvite)
admin.site.register(Entity)
