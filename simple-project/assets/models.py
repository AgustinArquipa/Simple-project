from django.db import models
from .managers import PatrimonyManager

# Create your models here.
class Patrimony(models.Model):
    number_patrimony = models.CharField(
        max_length=20,
        verbose_name="N° Patrimonial",
        null=False,
        blank=False,
        db_index=True
    )
    code = models.CharField(
        max_length=15,
        verbose_name="Codigo",
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=40,
        verbose_name="Ubicacíon",
        null=True,
        blank=True
    )

    objects = PatrimonyManager()

    class Meta:
        db_table = "Patrimonio"

    def __str__(self) -> str:
        return f"{self.number_patrimony}"
    
    def get_lockers(self):
        """
        Retorna todas las taquillas asociadas a este patrimonio
        """
        return self.assets.all()
        
    def to_json(self):
        item = {}
        item['id'] = self.id
        item['number_patrimony'] = self.number_patrimony
        item['location'] = self.location
        item['lockers'] = [locker.get_sticker() for locker in self.get_lockers()]
        return item