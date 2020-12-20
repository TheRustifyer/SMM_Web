from django.contrib import admin
from .models import UserData, RrssAccess, RrssApiKeys, RrssKeys

# Register your models here.
admin.site.register(UserData)
admin.site.register(RrssAccess)
admin.site.register(RrssApiKeys)
admin.site.register(RrssKeys)

