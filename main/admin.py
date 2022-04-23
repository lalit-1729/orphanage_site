from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Orphan)
admin.site.register(Event)
admin.site.register(Orphanage)
admin.site.register(Feedback)