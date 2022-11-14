from django.contrib import admin
from myApp.models import Roka,Prewedding,Shadi
# Register your models here.
class RokaAdmin(admin.ModelAdmin):
	l=['publish','created','updated','photo']
	ordering=['publish',]

class PreweddingAdmin(admin.ModelAdmin):
	l=['publish','created','updated','photo']
	ordering=['publish',]

class ShadiAdmin(admin.ModelAdmin):
	l=['publish','created','updated','photo']
	ordering=['publish',]

admin.site.register(Roka,RokaAdmin)
admin.site.register(Prewedding,PreweddingAdmin)
admin.site.register(Shadi,ShadiAdmin)