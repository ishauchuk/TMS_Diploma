from django.db import models
from itertools import chain
from django.db.models.query import QuerySet
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from datetime import timedelta


class Services(models.Model):
    # DURATION_CHOICES = [
    #                        (timedelta(days=0, hours=x, minutes=y, seconds=0,microseconds=0),
    #                         '{:02d}:{:02d}'.format(x, y))
    #                        for x in range(0, 3) for y in (0, 30)]
    DURATION_CHOICES = [
                           (datetime.time(hour=x, minute=y),
                            '{:02d}:{:02d}'.format(x, y))
                           for x in range(0, 2) for y in (0, 30)][1:]
    service_name = models.CharField(max_length=50, verbose_name="Услуга",
                                    primary_key=True)
    service_price = models.FloatField(validators=[MinValueValidator(0.0)],
                                      verbose_name="Цена")
    # service_duration = models.DurationField(choices=DURATION_CHOICES,
    #                                         verbose_name='Продолжительность')
    service_duration = models.TimeField(choices=DURATION_CHOICES,
                                        verbose_name='Продолжительность')

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.service_name


class Masters(models.Model):
    master_name = models.CharField(max_length=50, verbose_name="Имя")
    master_surname = models.CharField(max_length=50, verbose_name="Фамилия",
                                      primary_key=True)
    master_photo = models.ImageField(
        upload_to='api/static/master_photos/',
        default='api/static/master_photos/master_photo_default.jpg',
        verbose_name="Фото", null=True, blank=True,
    )
    master_phone = PhoneNumberField(unique=True, null=False, blank=False,
                                    verbose_name="Номер телефона",
                                    help_text='+375XX-XXX-XX-XX')
    master_skills = models.ManyToManyField(Services, verbose_name="Навыки")

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.master_name} {self.master_surname}'


class Clients(models.Model):
    # id = models.AutoField(primary_key=True)
    client_name = models.CharField(verbose_name='Имя', max_length=50)
    client_surname = models.CharField(verbose_name='Фамилия', max_length=50,
                                      primary_key=True)
    client_phone = PhoneNumberField(unique=True, null=False, blank=False,
                                    verbose_name="Номер телефона",
                                    help_text='+375XX XXX-XX-XX')
    info = models.TextField(verbose_name='Дополнительная информация',
                            blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.client_name} {self.client_surname}'


class Orders(models.Model):
    TIME_CHOICES = [
        (datetime.time(hour=x, minute=y), '{:02d}:{:02d}'.format(x, y))
        for x in range(9, 21) for y in (0, 30)]

    # TIME_CHOICES = [
    #                        (timedelta(days=0, hours=x, minutes=y, seconds=0, microseconds=0),
    #                         '{:02d}:{:02d} '.format(x, y))
    #                        for x in range(9, 21) for y in (0, 30)]

    # id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey(Services, null=True,
                                   on_delete=models.SET_NULL)
    order_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)],
        verbose_name='Дата посещения')
    order_time = models.TimeField(choices=TIME_CHOICES,
                                  verbose_name='Время посещения')
    # order_time = models.DurationField(choices=TIME_CHOICES,
    #                               verbose_name='Время посещения')
    master_choice = models.ForeignKey(Masters, null=True,
                                      on_delete=models.SET_NULL)
    client_choice = models.ForeignKey(Clients, null=True,
                                      on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if Orders.objects.filter(order_date=self.order_date,
                                 order_time=self.order_time,
                                 master_choice=self.master_choice):
            # return ValueError("Choose another date")
            raise ValidationError("The time is already taken!")
            # super(Orders, self).save(*args, **kwargs)
        print('if')
        # else:
        print(len(Orders.objects.filter(order_date=self.order_date,
                                        order_time=self.order_time)))
        # super().save()
        super(Orders, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.order_type} {self.client_choice}'
