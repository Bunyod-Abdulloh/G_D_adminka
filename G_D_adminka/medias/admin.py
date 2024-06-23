from django.contrib import admin
from .models import User, Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9, Table10, Tables


class CommonAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('lesson_number', 'file_name', 'caption')
    list_display_links = ('lesson_number', )
    ordering = ('lesson_number',)


class TablesAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('table_number', 'table_name', 'table_type', )
    list_display_links = ('table_name', )
    ordering = ('table_number',)


class Table9Admin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('sequence', 'subcategory', 'category',)
    list_display_links = ('subcategory',)
    ordering = ('id',)
    list_filter = ('category',)


class Table10Admin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('id', 'file_name',)
    list_display_links = ('file_name',)
    ordering = ('id',)


tables = [Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8]

for table in tables:
    admin.site.register(table, CommonAdmin)

admin.site.register(Table9, Table9Admin)
admin.site.register(Table10, Table10Admin)
admin.site.register(Tables, TablesAdmin)
admin.site.register(User)
