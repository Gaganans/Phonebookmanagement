from django.contrib import admin
from.models import*
# Register your models here.


class phonebookAdmin(admin.ModelAdmin):
    list_display=("Name","Number")

admin.site.register(phonebook1,phonebookAdmin)    