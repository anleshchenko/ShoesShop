from django.db import models
from django.utils.translation import ugettext as _


class Manufacturer(models.Model):
    name = models.CharField('Название производителя', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class Color(models.Model):
    name = models.CharField(_('ColorName'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


class Category(models.Model):
    name = models.CharField(_('CategoryName'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Shoes(models.Model):
    SKU = models.IntegerField(_('SKU'), blank=False)
    name = models.CharField(_('Name'), max_length=256, blank=False)
    manufacturer = models.ForeignKey(Manufacturer,
                                     default=None,
                                     blank=False,
                                     verbose_name=_('Manufacturer'),
                                     on_delete=models.SET_DEFAULT
                                     )
    color = models.ForeignKey(Color,
                              default=None,
                              blank=False,
                              verbose_name=_('Color'),
                              on_delete=models.SET_DEFAULT
                              )

    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=False)
    size = models.CharField(_('Size'), max_length=10, blank=False)
    category = models.ForeignKey(Category,
                                 default=None,
                                 blank=False,
                                 verbose_name=_('Category'),
                                 on_delete=models.SET_DEFAULT
                                 )

    def __str__(self):
        return f"{self.category}: {self.manufacturer} | {self.name}, {_('Price')}: ${self.price}"

    class Meta:
        verbose_name = _('Shoes')
        verbose_name_plural = _('Shoes')
