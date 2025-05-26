from datetime import datetime

def formatear_fecha(fecha_str):
    try:
        dt = datetime.strptime(fecha_str, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except:
        return fecha_str