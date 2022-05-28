# -*- coding: utf-8 -*-
import datetime

from django.forms import ModelForm, ChoiceField
from django import forms
from .models import Orders
from django.core.exceptions import NON_FIELD_ERRORS


class DateInput(forms.DateInput):
    input_type = 'date'


class OrdersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_type'].empty_label = "Услуга не выбрана"
        self.fields['order_time'].choices = [('', 'Время не выбрано')] + \
                                            self.fields['order_time'].choices[
                                            1:]
        self.fields['master_choice'].empty_label = "Мастер не выбран"

    class Meta:
        model = Orders
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': f"Мастер на это время уже занят",
            }
        }

        widgets = {
            'order_date': DateInput(),
        }

    # def clean(self):
    #     order_type = self.cleaned_data.get('order_type')
    #     master_choice = self.cleaned_data.get('master_choice')
    #     master = Masters.objects.filter(master_skills='стрижка мужская')
    #     print(master.values_list())

    # def clean(self):
    #
    #     order_type = self.cleaned_data.get('order_type')
    #     master_choice = self.cleaned_data.get('master_choice')
    #     for i in range(len(Masters.objects.all())):
    #         for j in Masters.objects.all()[i].master_skills.filter():
    #             print(j.service_name)
    #             if str(order_type) == str(j.service_name):
    #                 return self.cleaned_data
    #             else:
    #                 return HttpResponse("Этот мастер оказывает другие услуги")
    # print(Masters.objects.all()[i].master_skills.all())
    # m1 = Masters.objects.all()
    # for i in m1[0].master_skills.filter():
    #     print(i.service_name)
    # if master_choice == Masters.objects.all().filter(master_skills=order_type):
    #     print('no')
    #     print(master_choice)
    #     raise ValidationError("Workshop times overlap.")
    # return self.cleaned_data
    #     super(Orders, self).clean()
