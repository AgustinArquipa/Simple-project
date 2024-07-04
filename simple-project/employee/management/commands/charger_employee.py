
from django.core.management.base import BaseCommand, CommandParser
from ...utils import load_data_from_excel


class Command(BaseCommand):
    # Extendemos de la base BaseCommand
    help = "Carga empleado desde un arhivo CSV o XLSX"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv_file', type=str, help="La ruta al archivo CSV")

    def handle(self, *args, **kwargs ) -> str | None:
        name_file = kwargs['csv_file']
        load_data_from_excel(name_file)

        if not load_data_from_excel:
            # Hacemos una verificacion si se encontro el archivo
            self.stdout.write(self.style.ERROR('Error al cargar los datos.'))

        self.stdout.write(self.style.SUCCESS('Datos cargados correctamente.'))
