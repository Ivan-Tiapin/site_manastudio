from django.contrib import admin
from .models import AssetsDB, LibraryDB

# Register your models here.
admin.site.register(AssetsDB)
admin.site.register(LibraryDB)