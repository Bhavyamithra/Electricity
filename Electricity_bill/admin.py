from django.contrib import admin

# Register your models here.
from . models import User, Elec_provider, User_electricity, Subscription

admin.site.register(User)
admin.site.register(Elec_provider)
admin.site.register(User_electricity)
admin.site.register(Subscription)