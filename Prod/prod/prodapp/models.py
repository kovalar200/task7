from django.db import models
from django.core.validators import MinValueValidator

class Заказчик(models.Model):
    УИД = models.AutoField(primary_key=True)
    Наименование = models.CharField(max_length=255)
    ИНН = models.CharField(max_length=12, unique=True)
    Адрес = models.TextField()
    Телефон = models.CharField(max_length=20)

class Заказы(models.Model):
    УИД = models.AutoField(primary_key=True)
    ДатаДокумента = models.DateField()
    ЗаказчикУИД = models.ForeignKey(
        'Заказчик',
        on_delete=models.CASCADE,
        related_name='заказы'
    )

class Продукция(models.Model):
    УИД = models.AutoField(primary_key=True)
    Наименование = models.CharField(max_length=255)
    Единица_Измерения = models.CharField(max_length=50)
    Базовая_Цена = models.DecimalField(max_digits=10, decimal_places=2)


class Заказ_Продукция(models.Model):
    УИД = models.AutoField(primary_key=True)
    Заказ_Покупателя_УИД = models.ForeignKey(
        'Заказы',
        on_delete=models.CASCADE,
        related_name='продукция'
    )
    Продукция_УИД = models.ForeignKey(
        'Продукция',
        on_delete=models.CASCADE,
        related_name='заказы'
    )
    Количество = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    Цена = models.DecimalField(max_digits=10, decimal_places=2)
    Скидка = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    Итоговая_Сумма = models.DecimalField(max_digits=12, decimal_places=2)


class Спецификация(models.Model):
    УИД = models.AutoField(primary_key=True)
    Продукция_УИД = models.ForeignKey(
        'Продукция',
        on_delete=models.CASCADE,
        related_name='спецификации'
    )
    Наименование = models.CharField(max_length=255)
    Изготовитель = models.CharField(max_length=255)



class Материал(models.Model):
    УИД = models.AutoField(primary_key=True)
    Название = models.CharField(max_length=255)

class Заказы_На_Производство(models.Model):
    УИД = models.AutoField(primary_key=True)
    Номер_Документа = models.CharField(max_length=100)
    Дата_Запуска = models.DateField()
    Подразделение = models.CharField(max_length=255)
    Исполнитель = models.CharField(max_length=255)
    Материал_УИД = models.ForeignKey(
        'Материал',
        on_delete=models.CASCADE,
        related_name='производственные_заказы'
    )



class Заказы_На_Производство_Продукция(models.Model):
    УИД = models.AutoField(primary_key=True)
    Продукция_УИД = models.ForeignKey(
        'Продукция',
        on_delete=models.CASCADE,
        related_name='производственные_заказы'
    )
    Заказ_Производства_УИД = models.ForeignKey(
        'Заказы_На_Производство',
        on_delete=models.CASCADE,
        related_name='продукция'
    )
    Количество = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    Фактическая_Стоимость = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.Продукция_УИД} - {self.Количество}"