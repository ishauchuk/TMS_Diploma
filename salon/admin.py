from django.contrib import admin
from .models import Masters, Services, Clients, Orders
from rangefilter.filters import DateTimeRangeFilter
from django.utils.safestring import mark_safe


@admin.register(Masters)
class MastersAdmin(admin.ModelAdmin):
    list_display = ('master_surname', 'master_name', 'master_phone',
                    'get_html_master_photo')
    fields = ('master_name', 'master_surname', 'master_phone', 'master_photo',
              'get_html_master_photo', 'master_skills')
    filter_horizontal = ('master_skills',)
    readonly_fields = ('get_html_master_photo',)

    def get_html_master_photo(self, object):
        if object.master_photo:
            return mark_safe(
                f"<img src='{object.master_photo.url}' width=100>")

    get_html_master_photo.short_description = "Превью"


@admin.register(Services)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price', 'service_duration')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_surname')


@admin.register(Orders)
class OrdersTimeAdmin(admin.ModelAdmin):
    list_display = (
        'order_date', 'order_time', 'order_type', 'master_choice',
        'client_choice')
    list_filter = (
        ('order_time', DateTimeRangeFilter), 'master_choice', 'order_type')
