from django.db import models


class FirmName(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Firm name'
        verbose_name_plural = 'Firm names'


class FirmInfo(models.Model):
    name = models.ForeignKey(FirmName, on_delete=models.CASCADE, verbose_name='Firm name')
    price = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'firm: {str(self.name)}, {str(self.date)}' if self.name else ''

    class Meta:
        verbose_name = 'Firm info'
        verbose_name_plural = 'Firms info'
