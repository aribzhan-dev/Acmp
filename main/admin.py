from django.contrib import admin
from main.models import Language, Tasks, Clue, Comment, Trans

admin.site.register(Language)
admin.site.register(Tasks)
admin.site.register(Clue)
admin.site.register(Comment)

@admin.register(Trans)
class TransAdmin(admin.ModelAdmin):
    list_display = ('key', 'language', 'value')
    list_filter = ('language',)
    search_fields = ('key', 'value')



