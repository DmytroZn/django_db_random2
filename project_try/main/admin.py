from django.contrib import admin

# Register your models here.

from . models import Agregate

class AgregateAdmin(admin.ModelAdmin):
    list_display = ('number_of_controller', 't_delta', 't_input', 'zdate', 'ztime')

admin.site.register(Agregate, AgregateAdmin)