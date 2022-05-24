# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Orders


class DateInput(forms.DateInput):
    input_type = 'date'


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

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
