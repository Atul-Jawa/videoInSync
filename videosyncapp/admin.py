from django.contrib import admin
from .models import Group
from channels_presence.models import Room, Presence

# Register your models here.
admin.site.register(Room)
admin.site.register(Presence)
admin.site.register(Group)