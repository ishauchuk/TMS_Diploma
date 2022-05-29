# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Orders, Masters


class DateInput(forms.DateInput):
    input_type = 'date'


class OrdersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_type'].empty_label = "Услуга не выбрана"
        self.fields['order_time'].choices = [
                                                ('', 'Время не выбрано')] + \
                                            self.fields['order_time'].choices[
                                            1:]
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
        if master_choice not in Masters.objects.filter(
                master_skills=order_type):
            raise forms.ValidationError(
                "Выбранный мастер не оказывает данную услугу")
        if Orders.objects.filter(order_time=cleaned_data['order_time'],
                                 master_choice=cleaned_data['master_choice'],
                                 order_date=cleaned_data[
                                     'order_date']).exists():
            raise forms.ValidationError("Выбранный мастер занят")

        return cleaned_data
