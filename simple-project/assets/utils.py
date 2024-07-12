import os
import pandas as pd
from .models import Patrimony
from django.conf import settings

def load_data_from_csv(name_file):
    path_file = os.path.join(settings.BASE_DIR, 'documents', name_file)
    print("Ruta del archivo -> ", path_file)
    
    # Verificamos si el archivo existe
    if os.path.exists(path_file):
        print("El archivo si existe y si se encontro")
    
        # Leemos el archivo Excel
        df = pd.read_csv(path_file, encoding="utf-8",sep=";")

        # Iteramos sobre las filas del DataFrame
        for index, row in df.iterrows():
            number_patrimony = row['Numero Patrimonial']
            code = row['Codigo']
            location = row['Local']
            #print(number_patrimony, code, location)
            # Creamos un nuevo empleado o actualizamos uno existente
            patrimony, created = Patrimony.objects.update_or_create(
                number_patrimony=number_patrimony,
                defaults={
                    'code':code,
                    'location':location
                }
            )
    else:
        return 