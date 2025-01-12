from django.contrib import admin
from .models import Profile, NewUserEmailSettings

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	save_on_top = True
	search_fields = ['user']

class NewUserEmailSettingsAdmin(admin.ModelAdmin):
	list_display = ('subject', 'from_mail', 'to_mail')
	save_on_top = True
	search_fields = ['user']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(NewUserEmailSettings, NewUserEmailSettingsAdmin)