from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from myapp.models import Currency, Holding, CompatibleHoroscope
from django.contrib import admin
from .models import User1
class HoldingInLine(admin.TabularInline):
    fields = ('iso','value','buy_data')
    model = Holding
    extra = 0
class CurrencyAdmin(admin.ModelAdmin):
    fields = ('long_name','iso')
    inlines = [HoldingInLine]

admin.site.register(Currency,CurrencyAdmin)

class User1Admin(admin.ModelAdmin):
    list_display = ('name', 'horoscope')

admin.site.register(User1, User1Admin)

class CompatibleHoroscopeAdmin(admin.ModelAdmin):
    list_display = ('horoscope1','compatible_horoscope')

admin.site.register(CompatibleHoroscope, CompatibleHoroscopeAdmin)