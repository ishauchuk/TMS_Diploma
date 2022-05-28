import datetime
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Services(models.Model):
    DURATION_CHOICES = [
                           (datetime.time(hour=x, minute=y),
                            '{:02d}:{:02d}'.format(x, y))
                           for x in range(0, 2) for y in (0, 30)][1:]
    service_name = models.CharField(max_length=50, verbose_name="Услуга",
                                    primary_key=True)
    service_price = models.FloatField(validators=[MinValueValidator(0.0)],
                                      verbose_name="Цена")
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
        default='master_photo_default.jpg',
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


class Orders(models.Model):
    client_name = models.CharField(verbose_name='Имя', max_length=50)
    client_surname = models.CharField(verbose_name='Фамилия', max_length=50)
    client_phone = PhoneNumberField(null=False, blank=False,
                                    verbose_name="Номер телефона",
                                    help_text='+375XX XXX-XX-XX')
    TIME_CHOICES = [
        (datetime.time(hour=x, minute=y), '{:02d}:{:02d}'.format(x, y))
        for x in range(9, 21) for y in (0, 30)]
    order_type = models.ForeignKey(Services, null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name="Услуга")
    order_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)],
        verbose_name='Дата посещения')
    order_time = models.TimeField(choices=TIME_CHOICES,
                                  verbose_name='Время посещения')
    master_choice = models.ForeignKey(Masters, null=True,
                                      on_delete=models.SET_NULL,
                                      verbose_name='Мастер')

    client_phone.error_messages[
        'invalid'] = 'Проверьте правильность введенного номера телефона.'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        unique_together = ('order_time', 'master_choice', 'order_date')

    def __str__(self):
        return f'{self.order_type} {self.client_surname}'
