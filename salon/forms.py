# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Clients
from phonenumber_field.formfields import PhoneNumberField


# class AddOrder(forms.Form):
#     client_choice = forms.ForeignKey(Clients, null=True,
#                                       on_delete=models.SET_NULL)
#     TIME_CHOICES = [
#         (datetime.time(hour=x, minute=y), '{:02d}:{:02d}'.format(x, y))
#         for x in range(9, 21) for y in (0, 30)]
#     order_type = forms.ForeignKey(Services, null=True,
#                                    on_delete=models.SET_NULL,
#                                    verbose_name="Заказ")
#     order_date = forms.DateField(
#         validators=[MinValueValidator(datetime.date.today)],
#         verbose_name='Дата посещения')
#     order_time = forms.TimeField(choices=TIME_CHOICES,
#                                   verbose_name='Время посещения')
#     master_choice = forms.ForeignKey(Masters, null=True,
#                                       on_delete=models.SET_NULL,
#                                       verbose_name='Мастер')


# class DatePickerInput(forms.DateInput):
#     input_type = 'date'
#
#
# class TestForm(forms.ModelForm):
#     class Meta:
#     model = Orders
#     fields = ['order_date', 'order_time', 'order_type', 'master_choice',
#     'client_choice']
#
#     widgets = {
#         'order_date': DatePickerInput(),
#     }
#     model = Clients
#     fields = '__all__'


class AddClient(ModelForm):
    client_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    client_surname = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    client_email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    client_phone = PhoneNumberField(label="Номер телефона", widget=forms.TextInput(attrs={'placeholder': '+375 XX XXX-XX-XX'}))
    info = forms.TextInput()

    class Meta:
        model = Clients
        fields = ['client_name', 'client_surname', 'client_email', 'client_phone',
            'info']
        widgets = {
            'info': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }
