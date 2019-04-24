from django.contrib import admin
from .models import Reg
# Register your models here.
class Regadmin(admin.ModelAdmin):
    list_display = ['user','fname','lname','dob','mobno']
    list_filter = ['dob']
    class meta:
        model=Reg
admin.site.register(Reg,Regadmin)