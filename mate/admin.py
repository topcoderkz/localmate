from django.contrib import admin
from .models import User, Mate, Skill

# Register your models here.
admin.site.register(User)
admin.site.register(Mate)
admin.site.register(Skill)
