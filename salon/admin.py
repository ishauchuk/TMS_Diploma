from django.contrib import admin
from .models import Masters, Services, Clients, Orders


@admin.register(Masters)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('master_name', 'master_surname', 'master_phone')
    fields = ('master_name', 'master_surname', 'master_phone', 'master_photo',
              'master_skills')
    filter_horizontal = ('master_skills',)


@admin.register(Services)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price', 'service_duration')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_surname')


@admin.register(Orders)
class OrdersTimeAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'order_time', 'order_type', 'master_choice')
