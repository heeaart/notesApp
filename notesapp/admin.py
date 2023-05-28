from django.contrib import admin

from notesapp.models import Note


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'body', 'author')
