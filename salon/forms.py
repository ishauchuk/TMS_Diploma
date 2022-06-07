# -*- coding: utf-8 -*-
import datetime
from django.forms import ModelForm
from django import forms
from .models import Orders, Masters, Services

close_hour = 21
close_minutes = 0
close_time = datetime.datetime(100, 1, 1, close_hour, close_minutes, 0)


class DateInput(forms.DateInput):
    input_type = 'date'


class OrdersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_type'].empty_label = "Услуга не выбрана"
        self.fields['order_time'].choices = [
            ('', 'Время не выбрано')] + self.fields['order_time'].choices[1:]
        self.fields['master_choice'].empty_label = "Мастер не выбран"

    class Meta:
        model = Orders
        fields = '__all__'

        widgets = {
            'order_date': DateInput(),
        }

    def clean(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        order_type = self.cleaned_data.get('order_type')
        master_choice = self.cleaned_data.get('master_choice')
        order_time = self.cleaned_data.get('order_time')
        order_date = self.cleaned_data.get('order_date')

        if master_choice not in Masters.objects.filter(
                master_skills=order_type):
            raise forms.ValidationError(
                "Выбранный мастер не оказывает данную услугу")
        if Orders.objects.filter(order_time=cleaned_data['order_time'],
                                 master_choice=cleaned_data['master_choice'],
                                 order_date=cleaned_data[
                                     'order_date']).exists():
            raise forms.ValidationError("Выбранный мастер занят")

        order_duration = Services.objects.get(
            service_name=order_type).service_duration
        order_time_start = datetime.datetime(100, 1, 1, order_time.hour,
                                             order_time.minute,
                                             0)
        if (order_time_start + datetime.timedelta(
                hours=order_duration.hour,
                minutes=order_duration.minute)) > close_time:
            raise forms.ValidationError(
                "Мы не успеем все сделать до закрытия салона. Пожалуйста, выберите другое время")

        if order_date < datetime.date.today() or (
                datetime.datetime.now().date() == order_date and
                datetime.datetime(100, 1, 1, datetime.datetime.now().hour,
                                  datetime.datetime.now().minute,
                                  0) > order_time_start):
            raise forms.ValidationError(
                "У нас нет машины времени. Проверьте выбранную дату и/или время")

        other_orders = Orders.objects.filter(
            order_date=cleaned_data['order_date'],
            master_choice=cleaned_data[
                'master_choice'],
        )
        for order in other_orders:
            order_time_db = datetime.datetime(100, 1, 1, order.order_time.hour,
                                              order.order_time.minute, 0)
            order_time_dur_db = Services.objects.get(
                service_name=order.order_type).service_duration
            order_finish_db = (order_time_db + datetime.timedelta(
                hours=order_time_dur_db.hour,
                minutes=order_time_dur_db.minute)).time()
            if order_time_db.time() < order_time < order_finish_db:
                raise forms.ValidationError(
                    "Мастер занят в {:02d}:{:02d}, но готов принять Вас в {:02d}:{:02d}".format(
                        order_time.hour, order_time.minute,
                        order_finish_db.hour, order_finish_db.minute))

        return cleaned_data
