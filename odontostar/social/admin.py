from django.contrib import admin
from .models import SocialNetwork
# Register your models here.

class AdminSocialNetwork(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']


admin.site.register(SocialNetwork, AdminSocialNetwork)