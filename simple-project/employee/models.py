from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
STATUS_TYPES = [
    ('Monotributo', 'Monotributo'),
    ('Planta', 'Planta'),
    ('Planta Temporal.', 'Planta Temporal'),
    ('Contratado', 'Contratado')
]

class Employee(models.Model):
    full_name = models.CharField(
        max_length=60,
        db_index=True,
        verbose_name="Apellido y Nombre",
        null=True,
        blank=True
    )
    dni = models.CharField(
        max_length=10,
        db_index=True,
        verbose_name="Documento",
        null=True,
        blank=True
    )
    gruoping = models.CharField(
        max_length=25,
        verbose_name="Agrupamiento",
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Direccion",
        null=True,
        blank=True
    )
    service = models.CharField(
        max_length=100,
        verbose_name="Servicio",
        null=True,
        blank=True
    )
    status = models.CharField(
        verbose_name="Sit. Laboral",
        choices=STATUS_TYPES,
        default=STATUS_TYPES[1][0],
        null=True,
        blank=True
    )
    # box = models.CharField(
    #     verbose_name="Taquilla",
    #     max_length=15,
    #     null=True,
    #     blank=True
    # )
    # asset_number = models.CharField(
    #     verbose_name="N° Patrimonial",
    #     max_length=100,
    #     null=True,
    #     blank=True
    # )
    # unit = models.PositiveIntegerField(
    #     verbose_name="Cantidad Unitaria",
    #     null=True,
    #     blank=True,
    #     default=1,
    #     validators=[MinValueValidator(1), MaxValueValidator(50)],
    # )
    # location = models.CharField(
    #     verbose_name="Ubicacion",
    #     max_length=50,
    #     blank=True,
    #     null=True
    # )
    # code = models.CharField(
    #     max_length=30,
    #     verbose_name="Codigo",
    #     null=True,
    #     blank=True
    # )

    class Meta:
        db_table = "Empleado"

    def get_status_class(self):
        if self.status == "Monotributo":
            return 'bg-orange'
        elif self.status == "Planta":
            return 'bg-success'
        elif self.status == "Contratado":
            return 'bg-info'
        else:
            return 'bg-light'
        
    def get_full_name(self) -> str:
        return self.full_name

    def __str__(self) -> str:
        cad = f"{self.full_name} - {self.dni}"
        return cad

    def to_json(self):
        item = {}
        item['full_name'] = self.full_name
        item['dni'] = self.dni
        item['grouping'] = self.gruoping
        item['address'] = self.address
        item['service'] = self.service
        item['status'] = self.status
        return item