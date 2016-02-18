from django.db import models


class House(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    rent = models.DecimalField(max_digits=6, decimal_places=2)
    condominium_association_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    bedrooms = models.IntegerField()
    bathrooms= models.IntegerField()
    garage = models.IntegerField()
