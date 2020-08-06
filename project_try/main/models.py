from django.db import models

# Create your models here.

class Agregate(models.Model):
    number_of_controller = models.IntegerField(verbose_name='№ Контролдлера', null=True)
    t_delta = models.IntegerField(verbose_name='T дельта', null=True)
    t_input = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Температура входу', null=True)
    t_output = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Температура виходу', null=True)
    auto_hand = models.CharField(max_length=30, null=True)
    capacity = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Обєм', null=True)
    capacity_warm = models.DecimalField(max_digits=1000, decimal_places=2, verbose_name='Обєм тепла', null=True)
    capacity_current = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Обєм поточний', null=True)
    pressure = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='Тиск виходу', null=True)
    digital_input = models.IntegerField(verbose_name='Цифровий вхід', null=True)
    digital_output = models.IntegerField(verbose_name='Цифровий вихід', null=True)
    parameters = models.IntegerField(verbose_name='T дельта', null=True)
    w_accumulate = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='W накоп.', null=True)
    w_current = models.DecimalField(max_digits=1000, decimal_places=1, verbose_name='W пот.', null=True)
    zdate = models.DateField(verbose_name="Дата зони", null=True)
    ztime = models.TimeField(verbose_name="Час зони", null=True)

# a = Agregate(number_of_controller=2, t_delta=2, t_input=20, t_output=21, auto_hand='12', capacity=20, capacity_warm=125, capacity_current=12, pressure=12, digital_input=125, digital_output=15, parameters=15, w_accumulate=15, w_current=52, zdate=date(1995, 5, 6), ztime=time(10,54,20))

# a.save()


#
"""
from datetime import datetime, date, time, timedelta
import random




general_time = datetime(2001, 1, 2, 1, 1, 1)
for td in range(0, 51840):
    general_time +=  timedelta(seconds=5)
    for i in range(1, 51):

        a = Agregate(number_of_controller=i, t_delta=2, t_input=random.randrange(10, 29, 2), t_output=random.randrange(10, 29, 2), auto_hand='12', capacity=random.randrange(2, 10, 1), capacity_warm=random.randrange(2, 80, 1), capacity_current=random.randrange(2, 80, 1), pressure=random.randrange(2, 80, 1), digital_input=random.randrange(10, 30, 1), digital_output=random.randrange(2, 30, 1), parameters=15, w_accumulate=15, w_current=52, zdate=general_time.date(), ztime=general_time.time())
        a.save()
        print(f'date: {general_time.date()}, time: {general_time.time()}, agr: {i}')

"""
"""
g = datetime(2001, 1, 2, 1, 1, 1)
for l in range(0, 86400):
    g +=timedelta(seconds=5)
    for i in range(1, 51):
        print(f'date: {g.date()}, time{g.time()}, agr: {i}')
"""