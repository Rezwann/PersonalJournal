from django.urls import path
from PersonalJournal.views import journals_api

'''
Enables function in views.py through App.vue
'''
urlpatterns = [
    path('api/journals/', journals_api, name='journals api'),
]
