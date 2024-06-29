from django.db import models

# Create your models here.
STATUS_LOCKER = [
    ('Reservado', 'Reservado'),
    ('Ocupado', 'Ocupado'),
    ('Libre', 'Libre')
]

class Locker(models.Model):
    number_locker = models.CharField(
        max_length=6,
        verbose_name="Numero de Taquilla",
        null=True,
        blank=True
    )
    status_locker = models.CharField(
        max_length=25,
        verbose_name="Estado",
        choices=STATUS_LOCKER,
        null=True,
        blank=True
    )
    employee = models.ForeignKey(
        'employee.Employee',
        on_delete=models.CASCADE,
        related_name="lockers",
        verbose_name="Empleado",
        null=True,
        blank=True
    )
    patrimony = models.ForeignKey(
        'assets.Patrimony',
        on_delete=models.PROTECT,
        related_name="assets",
        verbose_name="Patrimonio",
        null=True,
        blank=True
    )

    class Meta:
        db_table = "Taquillas"

    def get_status_short(self):
        if self.status_locker == "Reservado":
            return 'R'
        elif self.status_locker == "Ocupado":
            return 'O'
        else:
            return 'L'

    def get_sticker(self) -> str:
        return f"{self.get_status_short() + self.number_locker}"

    def __str__(self) -> str:
        cad = f"{self.get_status_short()}-{self.number_locker} - Empleado: {self.employee.get_full_name()}" # Falta indicar que empleado tiene asociado
        return cad
    
    def to_json(self):
        item = {}
        item['id'] = self.id
        item['number_locker'] = self.number_locker
        item['status_locker'] = self.status_locker
        item['employee'] = self.employee.get_full_name() if self.employee else "Sin Empleado Asignado."
        item['patrimony'] = self.patrimony.number_patrimony
        return item