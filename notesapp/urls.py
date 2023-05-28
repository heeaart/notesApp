from django.urls import path

from notesapp.views import index

app_name = 'notesApp'

urlpatterns = [
    path('', index, name='index'),
]