"""
    Модели для сохранения данных 

    Returns:
        _type_: _description_
"""

from decimal import Decimal

from django.db import models


# # Create your models here.


class Workers(models.Model):
    """Модель данных, описывающая работника
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0))

    objects = models.Manager()

    def __str__(self):
        return f"{self.second_name} {self.name}"
