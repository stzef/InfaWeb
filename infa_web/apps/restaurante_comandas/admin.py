from django.contrib import admin

from infa_web.apps.restaurante_comandas.models import *


# Register your models here.
admin.site.register(Mesas)
admin.site.register(Meseros)
admin.site.register(Coda)
admin.site.register(Codadeta)
admin.site.register(Talocoda)
admin.site.register(Resupedi)
admin.site.register(Resupedipago)
