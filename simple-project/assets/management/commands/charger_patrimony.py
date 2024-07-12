from django.core.management.base import BaseCommand, CommandParser
from ...utils import load_data_from_csv

class Command(BaseCommand):
    # Extendemos de la BaseCommand
    help = "Carga Patrimonio desde un CSV o Excel"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv_file', type=str, help="Ruta del Archivo CSV")

    def handle(self, *args, **kwargs):
        name_file = kwargs['csv_file']
        load_data_from_csv(name_file)

        if not load_data_from_csv:
            # Hacemos una verificacion si se encontro el archivo
            self.stdout.write(self.style.ERROR('Error al cargar los datos.'))

        self.stdout.write(self.style.SUCCESS('Datos cargados correctamente.'))
