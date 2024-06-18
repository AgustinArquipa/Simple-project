
# Create here utils 

def getColumnsForModel(model, exclude_fields=None,include_fields=None):
    """
    Devuelve una lista con los verbose_name de los campos de la tabla para un modelo Django, excluyendo los campos especificos.
    Args:
        model (Model): Clase de modelo Django
        exclude_fields (list, optional): Lista de nombres de campos a excluir. Por defecto es None

    Returns:
        list: Lista con los verbose_name de los campos de la tabla
    """
    if exclude_fields is None:
        exclude_fields = []
    if include_fields is None:
        include_fields = []

    if include_fields:
        if exclude_fields:
            return [field.verbose_name for field in model._meta.get_fields()
                    if field.concrete and hasattr(field, 'verbose_name') and 
                    field.name in include_fields and field.name not in exclude_fields]
        else:
            return [field.verbose_name for field in model._meta.get_fields()
                    if field.concrete and hasattr(field, 'verbose_name') and field.name in include_fields]
    elif exclude_fields:
        return [field.verbose_name for field in model._meta.get_fields()
                if field.concrete and hasattr(field, 'verbose_name') and field.name not in exclude_fields]
    else:
        return [field.verbose_name for field in model._meta.get_fields()
                if field.concrete and hasattr(field, 'verbose_name')]