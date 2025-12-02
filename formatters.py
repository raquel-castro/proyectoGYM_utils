from datetime import date, datetime

def formatear_fecha(fecha) -> str:
    """Devuelve la fecha en formato dd/mm/yyyy si es date o datetime."""
    if isinstance(fecha, (date, datetime)):
        return fecha.strftime("%d/%m/%Y")
    return str(fecha)