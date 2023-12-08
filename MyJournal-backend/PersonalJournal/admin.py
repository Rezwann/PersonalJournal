from django.contrib import admin

# Register your models here.

from .models import PersonalJournal

admin.site.register(PersonalJournal)