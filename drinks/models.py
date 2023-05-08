from django.db import models


class Beer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Beer name',
    )
    brewery = models.CharField(
        max_length=255,
        verbose_name='Brewery name',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='Beer price',
    )
    fortress = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Beer fortress',
    )
    is_publish = models.BooleanField(
        default=False,
        verbose_name='Показать в меню'
    )

    def __str__(self):
        return f'{self.name} - {self.brewery}'

    class Meta:
        verbose_name = 'Пиво (Beer)'
        verbose_name_plural = 'Beers'
