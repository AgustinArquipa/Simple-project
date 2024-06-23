from django.db import models

# Create your models here.
STATUS_LOCKER = [
    ('Reservado', 'Reservado'),
    ('Ocupado', 'Ocupado')
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
        verbose_name="Empleado"
    )

    class Meta:
        db_table = "Taquillas"

    def get_status_short(self):
        if self.status_locker == "Reservado":
            return 'R'
        elif self.status_locker == "Ocupado":
            return 'O'
        else:
            return 'N/A'

    def __str__(self) -> str:
        cad = f"{self.get_status_short}-{self.number_locker} - Empleado: {self.employee.get_full_name()}" # Falta indicar que empleado tiene asociado