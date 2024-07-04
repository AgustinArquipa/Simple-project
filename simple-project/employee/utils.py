import os
import pandas as pd
from .models import Employee
from django.conf import settings

def load_data_from_excel(name_file):
    path_file = os.path.join(settings.BASE_DIR, 'documents', name_file)
    print("Ruta del archivo -> ", path_file)
    
    # Verificamos si el archivo existe
    if os.path.exists(path_file):
        print("El archivo si existe y si se encontro")
    
        # Leemos el archivo Excel
        df = pd.read_csv(path_file, encoding="utf-8",sep=";")
        # Reemplazamos las comas en la columna DNI
        df['DNI'] = df['DNI'].str.replace(',', '')

        # Iteramos sobre las filas del DataFrame
        for index, row in df.iterrows():
            dni = row['DNI']
            full_name = row['Nombre Completo']
            gruoping = row['Agrupacion']
            service = row['UG']
            status = row['SitLaboralCP']
            #print(dni, full_name, gruoping, service, status)
            # Creamos un nuevo empleado o actualizamos uno existente
            employee, created = Employee.objects.update_or_create(
                dni=dni,
                defaults={
                    'full_name':full_name,
                    'gruoping':gruoping,
                    'service':service,
                    'status':status
                }
            )
    else:
        return 