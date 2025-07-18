
class Servicio:
    """Modelo para representar un servicio registrado."""
    def __init__(self, cedula, cliente, descripcion, costo, forma_pago):
        self.cedula = cedula
        self.cliente = cliente
        self.descripcion = descripcion
        self.costo = float(costo)
        self.forma_pago = forma_pago

    def __str__(self):
        return f"{self.cedula} - {self.cliente} - {self.descripcion} - ${self.costo:.2f} - {self.forma_pago}"
