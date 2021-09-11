from django.contrib import admin
from finsure.models import Lender


class LenderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'active',
    )
    list_filter = ('active', )
    search_fields = (
        'pk',
        'name',
        'code',
    )


# REGISTER:

# Lender
admin.site.register(Lender, LenderAdmin)

# Site title
admin.site.site_header = 'Finsure Admin'
