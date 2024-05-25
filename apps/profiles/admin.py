from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date', 'profile_picture')
    search_fields = ('user__username', 'user__email', 'location')

admin.site.register(Profile, ProfileAdmin)
