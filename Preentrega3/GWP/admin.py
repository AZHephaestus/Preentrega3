from django.contrib import admin

from . import models

admin.site.register(models.game)
admin.site.register(models.gamegenre)
admin.site.register(models.gamebygenre)