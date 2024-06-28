from django.db import models

class PatrimonyManager(models.Manager):
    # Create here code
    def get_patrimony_already(self) -> bool:
        """
        Lo que trato de hacer con este metodo es que me devuelva si existe mas de un empleado en la BD
        return -> Devuelve V o F segun la consulta a la BD de Employee
        """
        return self.count > 1