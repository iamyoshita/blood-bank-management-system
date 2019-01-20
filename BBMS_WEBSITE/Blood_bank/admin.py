from django.contrib import admin

# Register your models here.
from .models import Donor, Bank, Receiver, Staff

admin.site.register(Donor)
admin.site.register(Bank)
admin.site.register(Receiver)
admin.site.register(Staff)
