from datetime import datetime

class Sismo:

    """Constructor de clase."""
    def __init__(self, fecha_hora: datetime, ubicacion: str, magnitud: float):
        self.fecha_hora: datetime = fecha_hora
        self.ubicacion: str = ubicacion
        self.magnitud: float = magnitud

    def generar_reporte(self) -> str:
        """Devuelve un mensaje formateado con los datos del sismo."""
        fecha_formateada = f"{self.fecha_hora.day}/{self.fecha_hora.month}/{self.fecha_hora.strftime('%y')}"
        hora_formateada = self.fecha_hora.strftime("%H:%M:%S")
        
        return (f"A las {hora_formateada} del {fecha_formateada} "
                f"hubo un seísmo de magnitud {self.magnitud:.1f} en {self.ubicacion}")


# PRUEBA DE INSTANCIACIÓN Y EJECUCIÓN
if __name__ == "__main__":
   
    fecha_evento = datetime(2026, 9, 28, 12, 30, 32)
    
    seismo_madrid = Sismo(
        fecha_hora=fecha_evento,
        ubicacion="Madrid",
        magnitud=2.0
    )
    
    resultado = seismo_madrid.generar_reporte()
    print(resultado)
