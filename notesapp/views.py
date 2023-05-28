from django.shortcuts import render

from notesapp.models import Note


# Create your views here.
def index(request):
    notes = Note.noteManager.all()
    return render(request, 'web/index.html', {'notes': notes})

