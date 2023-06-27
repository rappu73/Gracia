from django.db import models


class Task(models.Model):
    title = models.CharField('Задание', max_length=50)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

class Complex(models.Model):
    title = models.CharField('Название комплекса', max_length=100)
    price1 = models.CharField('Цена за 1 сеанс', max_length=50)
    price5 = models.CharField('Цена за 5 сеансов', max_length=50)
    price10 = models.CharField('Цена за 10 сеансов', max_length=50)
    task = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комплекс программ'
        verbose_name_plural = 'Комплекс программ'

class Massage(models.Model):
    title = models.CharField('Вид массажа', max_length=100)
    price1 = models.CharField('Цена за 1 сеанс', max_length=50)
    price5 = models.CharField('Цена за 5 сеансов', max_length=50)
    price10 = models.CharField('Цена за 10 сеансов', max_length=50)
    task = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массаж'

class Apparat(models.Model):
    title = models.CharField('Вид процедуры', max_length=100)
    price1 = models.CharField('Цена за 1 сеанс', max_length=50)
    price5 = models.CharField('Цена за 5 сеансов', max_length=50)
    price10 = models.CharField('Цена за 10 сеансов', max_length=50)
    task = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аппаратная процедура'
        verbose_name_plural = 'Аппаратные процедуры'
