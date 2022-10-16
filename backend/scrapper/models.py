from django.db import models

class CryptoData(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    one_hour = models.CharField(max_length=100)
    twentyfour_hour = models.CharField(max_length=100)
    seven_day = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    suppy = models.CharField(max_length=100)
    current_top_10 = models.BooleanField(default=False)

    def __str__(self):
        return self.name
